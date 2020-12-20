Data set Rad-6
==============
Files
-----
Rad-6_databases.xyz          : 10712 molecules with properties in XYZ format
Rad-6-RE_network.txt         : 32515 dissociation reactions
Trainingsetsplits.zip        : Sequences for FPS splits and random training set selection
MLmodels.zip                 : KRR coefficients for 98 ML models
README.txt                   : Documentation

Molecules: Rad-6_databases.xyz 
==============================
Geometry relaxations have been performed for 10712 molecules on DFT/PBE0 level
with tier-2 basis sets and pair-wise Tkatchenko-Scheffler van-der-Waals correction 
for dispersion interactions [1-4]. Molecules consist of H,C,O elements up to 6 heavy atoms.
The database comprises 9179 radical fragments and 1533 closed shell molecules.
Energies are calculated for low spin states (exceptions are C, O and O2). 
Additional single point calculations are performed with broken-symmetry DFT (BS-DFT)
at DFT/revPBE+D3/def2-TZVP level of theory [5-6]. 

Format
------
Molecules are stored in an extended ".xyz" file. It is an extension to a normal
".xyz" file in which one molecule is represented using the structure below. For
the extended format all molecules are concatenated within one file.  

Line       Content
----       -------
1          Number of atoms N
2          Properties I (for details see below)
3, ..., N  Element type, DFT coordinates (x, y, z) [Angstrom], UFF coordinates (x, y, z) [Angstrom]

The properties stored in the line below number of atoms:

I.  Property    Unit    Description
--  --------    ----    -----------
1   Properties  -       Description of the N lines below 
                        (element type, DFT coordinates, UFF coordinates) 
2   energy      eV      DFT energy of the present structure
3   AE          eV      Atomization energy of the present structure
4   id          -       Molecule id in database
5   smile       -       Smile string
6   BS-DFT      eV      Energy calculated with BS-DFT

Network: Rad-6-RE_network.txt
===============================
Reaction network of 32515 bond breaking reactions involving 10081 molecules from Rad-6.
Molecule A can either react to products B and C, i.e. A -> B + C (dissociation, type I) 
or molecule A reacts to molecule B, i.e. A -> B (rearrangement, type II). 

Format
------
Reactions are stored in a ".txt" file.

Column      Content
------      -------
1           Index of molecule A (id property in Rad-6_databases.xyz)
2           Index of molecule B (id property in Rad-6_databases.xyz)
3           Index of molecule C (id property in Rad-6_databases.xyz), reaction type I
            or "[x]", reaction type II
4           Reaction energy (RE) [eV], RE = sum(AE(products)) - AE(educt) 

Training, validation and test set splits: Trainingsetsplits.tar.xz
==================================================================
Sequences for random training set selection and intensive and extensive 
FPS splits. 

Directory structure
-------------------
Trainingsetsplits/ 
    -> fps_seq_av_ff_H.txt
    -> fps_seq_sum_ff_H.txt
    -> random_sampling_rad6.txt

Format
------
All three sequences are stored in individual ".txt" files as vectors. The numbers 
in the files are the indices of the molecules in Rad-6 (id properties). 
The last 1030 indices are the test set and 100 structures before the last 1030
are the validation set. Training sets of 500, 1000, 2000, 4000, 6000, 
8000 and 9582 configurations are used. 

fps_seq_av_ff_H.txt:        Intensive FPS split
fps_seq_sum_ff_H.txt:       Extensive FPS split
random_sampling_rad6.txt:   Random sampling


ML models: MLmodels.tar.xz
==========================
KRR coefficients for 98 ML models, including the extensive and 
intensive kernels with extensive and intensive FPS splits and 
random training set selection for both DFT and UFF geometries. 
Further the coefficients for Rad-6-BS models are included 
(intensive and extensive kernels with respective FPS splits 
and DFT geometries). For each category a learning curve has been made 
with 500, 1000, 2000, 4000, 6000, 8000 and 9582 training samples.   
AE/N mean values are additionally provided for the extensive and 
intensive fps splits and all training set sizes.

Directory structure
-------------------
MLmodels/
    -> K_ext_fps_ext_dft/
        -> Results_size_500_geos_dft_ktype_ext_mc_False_sigma_0.01/
            -> alpha_coeffs.txt
        -> Results_size_1000_geos_dft_ktype_ext_mc_False_sigma_0.005/
            -> alpha_coeffs.txt
        -> Results_size_2000_geos_dft_ktype_ext_mc_False_sigma_0.01/
            -> alpha_coeffs.txt
        -> Results_size_4000_geos_dft_ktype_ext_mc_False_sigma_0.001/
            -> alpha_coeffs.txt
        -> Results_size_6000_geos_dft_ktype_ext_mc_False_sigma_0.001/
            -> alpha_coeffs.txt
        -> Results_size_8000_geos_dft_ktype_ext_mc_False_sigma_5e-05/
            -> alpha_coeffs.txt
        -> Results_size_9582_geos_dft_ktype_ext_mc_False_sigma_0.0001/
            -> alpha_coeffs.txt
    -> K_ext_fps_ext_dft_bs/
        -> ...
    -> K_ext_fps_ext_uff/
        -> ...
    -> K_ext_fps_int_dft/
        -> ...
    -> K_ext_fps_int_uff/
        -> ...
    -> K_ext_fps_rand_dft/
        -> ...
    -> K_ext_fps_rand_uff/
        -> ...
    -> K_int_fps_ext_dft/
        -> ...
    -> K_int_fps_ext_uff/
        -> ...
    -> K_int_fps_int_dft/
        -> ...
    -> K_int_fps_int_dft_bs/
        -> ...
    -> K_int_fps_int_uff/
        -> ...
    -> K_int_fps_rand_dft/ 
        -> ...
    -> K_int_fps_rand_uff/
        -> ...
    -> AE_N_mean_values_fps_ext.txt
    -> AE_N_mean_values_fps_int_bs.txt
    -> AE_N_mean_values_fps_int.txt

Format:
-------
Coefficients are stored in named sub-directories (for details see II and III below) 
in "alpha_coeffs.txt" files as vectors.

II Sub-directories
------------------
Example I  : K_ext_fps_ext_dft/     i.e. extensive kernel, 
				    extensive FPS split and DFT geometries
Example II : K_int_fps_int_dft_bs/  i.e. intensive kernel, 
				    intensive FPS split and DFT geometries for Rad-6-BS

III Subsub-directories
----------------------
Example I : Results_size_500_geos_dft_ktype_ext_mc_False_sigma_0.01/    
	    i.e. training set size 500, DFT geometries, extensive kernel, 
	    no mean correction applied and regularization parameter 0.01.

"AE_N_mean_values_*.txt"
---------------------------
"AE_N_mean_values_*.txt" contain the average atomisation energy per atom for the 
individual training set sizes.

Column      Content
------      -------
1           training set size
2           mean AE/N [eV]

References
----------
[1] Blum, V.; Gehrke, R.; Hanke, F.; Havu, P.; Havu, V.; Ren, X.; Reuter, K.; Scheffler, M.Comput. Phys. Commun.2009,180, 2175 – 2196.
[2] Zhang, I. Y.; Ren, X.; Rinke, P.; Blum, V.; Scheffler, M.New J. Phys.2013,15, 123033.
[3] Adamo, C.; Barone, V.J. Chem. Phys.1999,110, 6158–6170.
[4] Tkatchenko, A.; DiStasio, R. A.; Car, R.; Scheffler, M.Phys. Rev. Lett.2012,108, 236402.
[5] Neese, F.WIREs Comput. Mol. Sci.2018,8, e1327.12. 
[6] Zhang, Y.; Yang, W.Phys. Rev. Lett.1998,80, 890.
