prefix=$1


obabel -ixyz ${prefix}.xyz -osmi > smiles-list.dat

python ../add-smile-2-xyz.py ${prefix} 
