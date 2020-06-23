This is a data set of 64 water molecules that is used as the training set of a neural network potential of water reported in
Cheng, Engel, Behler, Dellago & Ceriotti Ab initio thermodynamics of liquid
and solid water PNAS 2019

#
* step 1: generate soap descriptors

** use multisoap, the same setup as our multisoap gap fit. The `--peratom True` flag tell the script to dump atomic soap descriptors for each environment

gen_soap_descriptors.py -fxyz dataset_1593_eVAng.xyz -param_path two_soap_gap_fit_param --peratom true

** single soap
gen_soap_descriptors.py -fxyz dataset_1593_eVAng.xyz -param_path two_soap_gap_fit_param --peratom true

** smart soap, the default setup of the ASAP package
gen_soap_descriptors.py -fxyz dataset_1593_eVAng.xyz -param_path smart --peratom true

* step 2: linear ridge regression

** multisoap
ridge_regression.py -fxyz ASAP-soapparam-two_soap_gap_fit_param.xyz -fmat SOAPPARAM-two_soap_gap_fit_param -fy TotEnergy -prefix two_soap_gap_fit_param

** single soap
ridge_regression.py -fxyz ASAP-soapparam-one_soap_gap_fit_param.xyz -fmat SOAPPARAM-one_soap_gap_fit_param -fy TotEnergy -prefix one_soap_gap_fit_param

** smart soap
ridge_regression.py -fxyz ASAP-soapparam-smart.xyz -fmat SOAPPARAM-smart -fy TotEnergy --prefix soap-smart

* step 3 (optional): visualize
pca.py -fxyz ASAP-soapparam-smart.xyz -fmat SOAPPARAM-smart -colors TotEnergy



* to sparsify dataset

One can use the "frame_select" function in the ASAP package, probably better to start with a random selection