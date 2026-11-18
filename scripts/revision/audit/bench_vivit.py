"""Time one ViViT-B training step per precision / attention kernel / batch size (REVISION_LOG §7.4).

Random inputs of the real shape (32 frames, 3 x 224 x 224), AdamW, one forward +
backward + optimizer step, averaged over --steps after one warm-up step. Run
on one idle GPU. 2026-10-17 on a TITAN X (Pascal): fp16 + SDPA 22.7 s per batch
of 3; at batch 1, fp16 10.85 s vs. fp32 1.65 s (fp32 batch 3 and eager
attention batch 3 run out of memory in 12 GB).

Usage:
    CUDA_VISIBLE_DEVICES=0 python scripts/revision/audit/bench_vivit.py
"""

from __future__ import annotations

import argparse
import time

import torch
from transformers import VivitForVideoClassification

CHECKPOINT = "google/vivit-b-16x2-kinetics400"


def bench(autocast_dtype, attn: str, batch: int, steps: int) -> str:
    model = VivitForVideoClassification.from_pretrained(
        CHECKPOINT, num_labels=50, ignore_mismatched_sizes=True, attn_implementation=attn
    ).cuda().train()
    opt = torch.optim.AdamW(model.parameters(), lr=1e-5)
    x = torch.randn(batch, 32, 3, 224, 224, device="cuda")
    y = torch.randint(0, 50, (batch,), device="cuda")
    scaler = torch.amp.GradScaler(enabled=autocast_dtype is torch.float16)
    times = []
    for _ in range(steps + 1):
        torch.cuda.synchronize()
        t = time.time()
        with torch.autocast("cuda", dtype=autocast_dtype or torch.float32, enabled=autocast_dtype is not None):
            loss = model(pixel_values=x, labels=y).loss
        scaler.scale(loss).backward()
        scaler.step(opt)
        scaler.update()
        opt.zero_grad()
        torch.cuda.synchronize()
        times.append(time.time() - t)
    peak = torch.cuda.max_memory_allocated() / 2**30
    del model, opt
    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats()
    name = "fp16" if autocast_dtype is torch.float16 else "fp32"
    return f"{name} attn={attn} batch={batch}: {sum(times[1:]) / steps:.2f} s per step (peak {peak:.1f} GB)"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--steps", type=int, default=3)
    args = parser.parse_args()
    configs = [(torch.float16, "eager", 3), (torch.float16, "sdpa", 3), (None, "eager", 3), (None, "sdpa", 3),
               (torch.float16, "sdpa", 1), (None, "sdpa", 1)]
    for dtype, attn, batch in configs:
        try:
            print(bench(dtype, attn, batch, args.steps), flush=True)
        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()
            print(f"{'fp16' if dtype else 'fp32'} attn={attn} batch={batch}: out of memory", flush=True)


if __name__ == "__main__":
    main()
