prefix=$1

for str in *bmol*.json; do name=${str#*-}; mv $str ${prefix}-${name}; done
python /rds/project/t2_vol5/rds-t2-cs061/linear-regression-benchmarks/join.py --dataset ${prefix}
