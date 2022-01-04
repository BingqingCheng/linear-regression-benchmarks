dir=$(pwd); 
for a in $(awk '!/#/{print $0}' mol_systems.list); do 
	echo $a; 
	name=$(echo $a | sed 's/\//_/g'); 
	echo $name; 
	cd $a; 
	python3 $dir/extract_kernel.py -p $name 
	wait; 
	cd $dir; 
done
