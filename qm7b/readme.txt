
Data set dsgdb7njp
==================

14 electronic properties for 7k small organic molecules.

Please cite this publication if you use this data set:
* Gr\'egoire Montavon, Matthias Rupp, Vivekanand Gobre, Alvaro Vazquez-Mayagoitia,
  Katja Hansen, Alexandre Tkatchenko, Klaus-Robert M"uller, O. Anatole von Lilienfeld:
  Machine learning of molecular electronic properties in chemical compound space,
  New Journal of Physics, 15(9): 095003, IOP Publishing, 2013.
  DOI: 10.1088/1367-2630/15/9/095003

Related publications:
* Matthias Rupp, Alexandre Tkatchenko, Klaus-Robert M"uller, O. Anatole von 
  Lilienfeld: Fast and Accurate Modeling of Molecular Atomization Energies with 
  Machine Learning, Physical Review Letters, 108(5): 058301, 2012. 
  DOI: 10.1103/PhysRevLett.108.058301
* Gr\'egoire Montavon, Katja Hansen, Siamac Fazli, Matthias Rupp, Franziska
  Biegler, Andreas Ziehe, Alexandre Tkatchenko, O. Anatole von Lilienfeld,
  Klaus-Robert M"uller: Learning Invariant Representations of Molecules for
  Atomization Energy Prediction, Advances in Neural Information Processing 
  Systems 25 (NIPS 2012), Lake Tahoe, Nevada, USA, December 3-6, 2012.

A version of this data set with pre-calculated Coulomb matrices is available at
http://quantum-machine.org (last accessed 2013-04-08).

Files
-----

dsgdb7njp.xyz          - Molecules and properties in XYZ format.
dsgdb7njp_cvsplits.txt - Indices of 5-fold stratified cross-validation splits.
dsgdb7njp_subset1k.txt - Indices of stratified subsets of 1000 molecules.
readme.txt             - Documentation.

Molecules
---------

A subset of 7211 small organic molecules from the GDB-13 database [1]. It
contains all molecules with up to 7 non-hydrogen atoms and elements H,C,N,O,S,Cl.
Molecular geometries were generated using the universal force field [2] as
implemented in OpenBabel [3] and subsequently relaxed using the PBE 
approximation [4] to Kohn-Sham density functional theory [5] as implemented in 
FHI-aims [6]. Coordinates are in Angstrom; to convert to atomic units, multiply 
by 100/52.917720859.

Properties
----------

I. Identifier Unit       Description
-- ---------- ---------- -----------
01 ae_pbe0    kcal/mol   Atomization energy (DFT/PBE0)
02 p_pbe0     Angstrom^3 Polarizability (DFT/PBE0)
03 p_scs      Angstrom^3 Polarizability (self-consistent screening)
04 homo_gw    eV         Highest occupied molecular orbital (GW)
05 homo_pbe0  eV         Highest occupied molecular orbital (DFT/PBE0)
06 homo_zindo eV         Highest occupied molecular orbital (ZINDO/s)
07 lumo_gw    eV         Lowest unoccupied molecular orbital (GW)
08 lumo_pbe0  eV         Lowest unoccupied molecular orbital (DFT/PBE0)
09 lumo_zindo eV         Lowest unoccupied molecular orbital (ZINDO/s)
10 ip_zindo   eV         Ionization potential (ZINDO/s)
11 ea_zindo   eV         Electron affinity (ZINDO/s)
12 e1_zindo   eV         First excitation energy (ZINDO)
13 emax_zindo eV         Maximal absorption intensity (ZINDO)
14 imax_zindo arbitrary  Excitation energy at maximal absorption (ZINDO)

I. = Index, DFT/PBE0 = density functional theory with PBE0 functional,
GW = Hedin's GW approximation, ZINDO = Zerner's intermediate neglect of 
differential overlap. Divide ae_pbe0 by 23.045108 to convert to eV.

Cross-validation splits
-----------------------

Indices (starting from 1) for 5-fold stratified cross-validation are provided
for each property. Stratification is by property so that each fold covers
the whole property range. 

1k subset
---------

Indices (starting from 1) for a stratified subset of 1000 molecules are 
provided for each property. Stratification is by property so that the subset
covers the whole property range.

References
----------

[1] Lorenz C. Blum, Jean-Louis Reymond: 970 Million Druglike Small Molecules
    for Virtual Screening in the Chemical Universe Database GDB-13, Journal of
    the American Chemical Society 131(25): 8732-8733, 2009. DOI: 10.1021/ja902302h
[2] Anthony K. Rapp\'e, Carla J. Casewit, K. S. Colwell, William A. Goddard III,
    W. Mason Skiff: UFF, a full periodic table force field for molecular 
    mechanics and molecular dynamics simulations, Journal of the American
    Chemical Society 114(25): 10024-10035, 1992. DOI: 10.1021/ja00051a040
[3] Rajarshi Guha, Michael T. Howard, Geoffrey R. Hutchison, Peter Murray-Rust,
    Henry Rzepa, Christoph Steinbeck, J"org Wegner, Egon L. Willighagen: The 
    Blue Obelisk - Interoperability in Chemical Informatics, Journal of 
    Chemical Information and Modeling 46(3): 991-998, 2006. DOI: 10.1021/ci050400b
[4] John P. Perdew, Kieron Burke, Matthias Ernzerhof: Generalized Gradient 
    Approximation Made Simple, Physical Review Letters 77(18): 3865-3868, 1996.
    DOI: 10.1103/PhysRevLett.77.3865
[5] Walter Kohn, Lu J. Sham: Self-consistent equations including exchange and
    correlation effects, Physical Review 140(4A): A1133-A1138, 1965. 
    DOI: 10.1103/PhysRev.140.A1133
[6] Volker Blum, Ralf Gehrke, Felix Hanke, Paula Havu, Ville Havu, Xinguo Ren,
    Karsten Reuter, Matthias Scheffler: Ab initio molecular simulations with 
    numeric atom-centered orbitals, Computer Physics Communications 180(11):
    2175-2196, 2009. DOI: 10.1016/j.cpc.2009.06.022
