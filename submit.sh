#!/bin/bash
#SBATCH --account CHENG-SL3-CPU
#SBATCH --partition skylake-himem
#SBATCH --nodes 1
#SBATCH --ntasks 32
#SBATCH --time 12:00:00
#SBATCH -J benchml

#module purge
module load rhel7/default-peta4

module load anaconda/3.2019-10
conda init bash

source ~/.bashrc

prefix=$1

#for a in *log; do nline=$(wc -l $a | awk '{print $1}'); if [ $nline -le 100 ]; then rm $a; fi;  done

n=0

for m in $(grep '\- ' /rds/project/t2_vol5/rds-t2-cs061/linear-regression-benchmarks/model_list_on_csd3.txt | awk '{print $2}' | grep 'bmol' | shuf); do

if [ ! -e is_csh-${m}.json ] && [ -e ${m}.log ] && [ $n -lt 2 ] ; then
#if [ ! -e ${m}.log ] && [ $n -lt 1 ] ; then

((n++))
	bml -m benchmark --meta meta.json --models "^${m}$" --benchmark_json ${prefix}-${m}.json --use_ase &> ${m}.log &
fi
done

wait


