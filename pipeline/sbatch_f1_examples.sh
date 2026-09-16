#!/usr/bin/env bash
# Minimal Slurm sketches for frame F1 — EDIT partition/account/qos for your site.
# Usage idea: submit three jobs with dependencies after:
#   set -a && source config/local.env && set +a
# Does NOT run anything until you sbatch it. Print-first culture still applies inside each script (RUN=1).

# #SBATCH --job-name=fa_f1a
# #SBATCH --cpus-per-task=16
# #SBATCH --mem=32G
# #SBATCH --time=12:00:00
# #SBATCH --partition=YOUR_PARTITION
# set -a && source "$REPO_ROOT/config/local.env" && set +a
# RUN=1 bash "$REPO_ROOT/pipeline/F1_diamond.sh"

# After F1a succeeds, submit F1b (eggNOG; script name F2_eggnog.sh = frame F1 step 2):
# sbatch --dependency=afterok:<F1a_JOBID> --job-name=fa_f1b --cpus-per-task=16 --mem=64G --time=24:00:00 \
#   --wrap='set -a && source config/local.env && set +a && RUN=1 bash pipeline/F2_eggnog.sh'

# Then F1c InterProScan (needs INTERPROSCAN_HOME; often 64–128G, long walltime):
# sbatch --dependency=afterok:<F1b_JOBID> --job-name=fa_f1c --cpus-per-task=16 --mem=128G --time=48:00:00 \
#   --wrap='set -a && source config/local.env && set +a && RUN=1 bash pipeline/F3_interproscan.sh'

echo "This file is documentation-in-shell. Uncomment/adapt SBATCH lines for your cluster."
