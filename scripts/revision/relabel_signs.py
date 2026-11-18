"""Relabel the per-sign outputs of prediction_metrics.py with the sign names of the LSC50 data descriptor (Table 2).

The sign number in the file names (SSSS_VVVV_RRRR) is the class number of Table 2 of Florez-Sierra et al. 2024
("The first four digits symbolize the class number (Sign N presented in the Table 2)"); the IMU Timestamps.xlsx
lists the signs in the same order. The original workspace's correspondance.json, used until 2026-11-03, is a
different order (the unsorted listing of the IMU sign folders) and gave wrong names. Only names change: every
output is indexed by sign number, so no metric changes.

Usage: python relabel_signs.py <prediction_metrics dir> <sign_names_lsc50_table2.json>
"""
import glob, json, os, shutil, sys
import pandas as pd

d, table2 = sys.argv[1], sys.argv[2]
new = json.load(open(table2)); new = [new[str(i)] for i in range(50)]
old_json = os.path.join(d, "sign_names.json")
keep = os.path.join(d, "sign_names_correspondance_original.json")
if not os.path.exists(keep):
    shutil.copy(old_json, keep)

# old display names, in sign-number order, exactly as prediction_metrics.py wrote them (confusion CSV header)
ref = pd.read_csv(os.path.join(d, "confusion_late_fusion_slowfast_spoter_loso.csv"), index_col=0)
old = list(ref.columns)
if old == new:
    sys.exit("already relabelled")
o2n = dict(zip(old, new)); assert len(o2n) == 50

for f in sorted(glob.glob(os.path.join(d, "confusion_*.csv"))):
    cm = pd.read_csv(f, index_col=0)
    assert list(cm.columns) == old and list(cm.index) == old, f
    cm.columns, cm.index = new, new
    cm.to_csv(f)

ps = pd.read_csv(os.path.join(d, "per_sign_f1.csv"))
ps["sign"] = ps["sign_id"].map(lambda i: new[int(i)])
ps.to_csv(os.path.join(d, "per_sign_f1.csv"), index=False)

tc = pd.read_csv(os.path.join(d, "top_confusions_loso.csv"))
for c in ("true_sign", "predicted_as"):
    tc[c] = tc[c].map(o2n)
assert tc.notna().all().all()
tc.to_csv(os.path.join(d, "top_confusions_loso.csv"), index=False)

json.dump({str(i): n for i, n in enumerate(new)}, open(old_json, "w"), ensure_ascii=False)
print("relabelled", d)
