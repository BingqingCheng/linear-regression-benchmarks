#!/bin/bash
#SBATCH --account T2-CS061-CPU   
## CHENG-SL3-CPU
#SBATCH --partition skylake-himem
#SBATCH --nodes 1
#SBATCH --ntasks 1
##SBATCH --mem=256000
#SBATCH --time 36:00:00
#SBATCH -J benchml

#module purge
module load rhel7/default-peta4

module load anaconda/3.2019-10
conda init bash

source ~/.bashrc

prefix=$1
m=$2

bml -m benchmark --meta meta.json --models "^${m}$" --benchmark_json ${prefix}-${m}.json --use_ase &> ${m}.log &

wait


