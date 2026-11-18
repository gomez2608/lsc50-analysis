#!/bin/bash
# Wait for the SlowFast queue; rerun (up to 2 more passes) every SlowFast job that has no result (e.g. CUDA OOM when
# another user's jobs grew on a shared GPU), via the same launcher (it skips finished jobs); then fuse.
set -u
cd ~/lsc-revision/lsc50-cpu
O=~/lsc-revision/WORK/fusion
until [ -f $O/DONE_slowfast ]; do sleep 300; done
for attempt in 1 2; do
  missing=$(cut -d"|" -f1 $O/slowfast_jobs.txt | while read -r n; do [ -f $O/slowfast/slowfast-$n.json ] || echo $n; done)
  [ -z "$missing" ] && break
  echo "[$(date "+%F %H:%M")] retry pass $attempt: $(echo $missing)" | tee -a $O/slowfast.log
  for n in $missing; do rm -rf $O/claims/$n; done
  rm -f $O/DONE_slowfast
  scripts/revision/run_fusion.sh slowfast ../venv-slowfast/bin/python ../slowfast/clips $O ../slowfast_v2/selected_lr.txt
done
scripts/revision/run_fusion.sh fuse ../venv/bin/python $O ../WORK/spoter ../slowfast_v2/results
