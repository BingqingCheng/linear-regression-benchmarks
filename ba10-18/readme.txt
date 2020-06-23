
Data set ba10-18 / DFT-10B
==========================

Energies for 10*1595 binary alloy structures.

Supplementary data for

Chandramouli Nyshadham, Matthias Rupp, Brayden Bekker, Alexander V. Shapeev,
Tim Mueller, Conrad W. Rosenbrock, G{\'a}bor Cs{\'a}nyi, David W. Wingate,
Gus L.W. Hart: General Machine-Learning Surrogate Models for Materials Prediction,
arXiv 1809.09203, 2018.

Please cite above preprint if you use this dataset.

Files
-----

ba10-18.xyz - Alloys and properties in an extended XYZ format
readme.txt  - Explanations, this file

Structures
----------

10 binary alloys (AgCu, AlFe, AlMg, AlNi, AlTi, CoNi, CuFe, CuNi, FeV, NbNi)
with 10 different species and all possible face-centered cubic (fcc), body-
centered cubic (bcc) and hexagonal close-paced (hcp) structures up to 8 atoms
in the unit cell. 15,950 structures in total. Lattice parameters were set
according to Vegard's rule. Atom coordinates are given in Angstrom. The last
three lines of each structure contain the unit cell basis vectors.

Properties
----------

Energies were computed at density functional level of theory using projector-
augmented wave potentials and the PBE generalized gradient approximation
functional. k-point meshes constructed using generalized regular grids.

I.  Property  Unit  Description
--  --------  ----  -----------
 1  name      none  unique identifier, alloy elements and consecutive index
 2  lattice   none  lattice type of structure, either fcc, bcc or hcp
 3  te        eV    total energy
 4  fe        eV    enthalpy of formation, te minus sum of free atom energies

I. = Index

Please see the manuscript for further details.
