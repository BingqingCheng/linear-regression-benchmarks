
Water monomer @ PBE, PBE0, BLYP
-------------------------------

watergrid_60_HOH_180__0.7_rOH_1.8_vario_BLYP_AV5Z_delta_PS.xyz
watergrid_60_HOH_180__0.7_rOH_1.8_vario_PBE0_AV5Z_delta_PS.xyz
watergrid_60_HOH_180__0.7_rOH_1.8_vario_PBE_AV5Z_delta_PS.xyz

Each of these three files is a grid on the water monomer geometry, with extra
resolution near the minimum, altogether 6900 geometries in each file. Energy and
forces are computed with BLYP, PBE and PBE0 using the AV5Z basis set. Correspon-
ding values of Partridge-Schwenke potential energy surface are also included.

Water dimers @ MP2 / AVDZ, AVTZ, AVQZ
-------------------------------------

pef_m_ad_nf_n12_cp_1-10000.xyz.bz2
pef_m_aq_nf_n12_cp_1-1000.xyz.bz2
pef_m_at_nf_n12_cp_1-10000.xyz.bz2

Water dimer data, with O-O distances < 4.5 A. These are interaction energies
(total energy minus the monomer energies, with counterpoise correction for BSSE).
The configurations are decorrelated samples from a 300K MD trajectory with the
AMOEBA forcefield. The energies and forces are computed with MP2, at the AVDZ
(10k configurations), AVTZ (10k configurations) and AVQZ (1k configurations) level.

water_dimers_amoeba_bulk300K_1000_4.5_lt_Roo_lt_6.0_MP2_AVTZ.xyz

1k water dimers, with O-O distances between 4.5 and 6.0 A, sampled from a 300K
molecular dynamics simulation with the AMOEBA force field, and computed using
MP2/AVTZ, with total energies and forces, and also the monomer data with
counterpoise correction.

water_conf_0.02_dimer_dft_samples_4000K_Roo_lt_4.5A_MP2_AVTZ_2041-4080.xyz

2040 water dimers with O-O distance < 4.5 A, where the configurations come from
a 4000K DFT MD simulation with a weak confining potential. The energies and
forces are computed with MP2 at AVTZ level, and both dimer and monomer quantities
are provided with counterpoise correction.

pe_c-mp2_ad_nf_n12_cp_1-800.xyz

Water dimers @ MP2/AVDZ and CCSD(T)/AVDZ
----------------------------------------

800 water dimers, with total energies computed with MP2 and CCSD(T) using the
AVDZ basis set. These dimers come from a 300K MD simulation using the AMOEBA
force field.
