import sys
from ase.io import read, write

def main(prefix):

    smiles = [ ln.split()[0] for ln in open('smiles-list.dat').readlines() ]
    configs = read(prefix+'.xyz', ':')
    print('No. smile string: ', len(smiles), 'No. xyz: ', len(configs))
    assert len(smiles) == len(configs)
    for config, smi in zip(configs, smiles): 
        config.info["smiles"] = smi
        if 'force' in config.arrays.keys(): del config.arrays['force']
    write(prefix+'_w_smiles.xyz', configs)

if __name__ == '__main__':
   main(sys.argv[1])
