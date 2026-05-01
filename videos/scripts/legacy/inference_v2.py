import av
import numpy as np
import torch
import os

from datasets import Dataset

from transformers import VivitImageProcessor, VivitForVideoClassification, Trainer, TrainingArguments
from huggingface_hub import hf_hub_download

np.random.seed(0)


def read_video_pyav(container, indices):
    '''
    Decode the video with PyAV decoder.
    Args:
        container (`av.container.input.InputContainer`): PyAV container.
        indices (`List[int]`): List of frame indices to decode.
    Returns:
        result (np.ndarray): np array of decoded frames of shape (num_frames, height, width, 3).
    '''
    frames = []
    container.seek(0)
    start_index = indices[0]
    end_index = indices[-1]
    for i, frame in enumerate(container.decode(video=0)):
        if i > end_index:
            break
        if i >= start_index and i in indices:
            frames.append(frame)
    return np.stack([x.to_ndarray(format="rgb24") for x in frames])


def sample_frame_indices(frame_sample_rate, seg_len):
    '''
    Sample a given number of frame indices from the video.
    Args:
        clip_len (`int`): Total number of frames to sample.
        frame_sample_rate (`int`): Sample every n-th frame.
        seg_len (`int`): Maximum allowed index of sample's last frame.
    Returns:
        indices (`List[int]`): List of sampled frame indices
    '''
    indices = np.arange(0, seg_len, frame_sample_rate).astype(np.int64)
    
    return indices


file_path = os.path.join(os.getcwd(),"LSC","VIDEOS","COLOR_BODY","0000_0000_0001.avi")

container = av.open(file_path)

indices = sample_frame_indices(frame_sample_rate=container.streams.video[0].frames/32, seg_len=container.streams.video[0].frames)
video = read_video_pyav(container=container, indices=indices)

image_processor = VivitImageProcessor.from_pretrained("google/vivit-b-16x2-kinetics400")
model = VivitForVideoClassification.from_pretrained("google/vivit-b-16x2-kinetics400")

inputs = image_processor(list(video), return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# model predicts one of the 400 Kinetics-400 classes
predicted_label = logits.argmax(-1).item()
print(model.config.id2label[predicted_label])


def load_videos_from_directory(directory):
    video_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.avi')]
    data = {'video_path': video_files}
    return Dataset.from_dict(data)


print("LOADING DATASET")

video_directory = os.path.join(os.getcwd(), "LSC", "VIDEOS", "COLOR_BODY")
dataset = load_videos_from_directory(video_directory)


def preprocess_function(examples):
    print(len(examples["video_path"]))

    videos = []

    for route in examples["video_path"]:
        container = av.open(route)
        indices = sample_frame_indices(frame_sample_rate=container.streams.video[0].frames/32, seg_len=container.streams.video[0].frames)
        video = read_video_pyav(container=container, indices=indices)
        inputs = image_processor(list(video), return_tensors="pt")
        videos.append(inputs)
    return inputs

print("PREPROCESSING DATASET")
dataset = dataset.map(preprocess_function, batched=True)

training_args = TrainingArguments(
    output_dir="./vivit-finetuned-2701",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=1e-4,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=4,
    num_train_epochs=30,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    eval_dataset=dataset,  # Use a separate validation dataset if available
)

print("TRAINING")
trainer.train()