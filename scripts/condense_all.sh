dir=$(pwd); for a in $(awk '!/#/{print $0}' mol_systems.list); do echo $a; name=$(echo $a | sed 's/\//_/g'); echo $name; cd $a; bash $dir/condense.sh $name; wait; cd $dir;  done
