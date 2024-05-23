# SNR_calculation

Python script to analyse the signal-to-noise-ratio (SNR) from two recontructed DICOM files. The main function **SNR_compute** read a Nifti file, create a mask for noise analysis and compute the SNR. It also provide information for each channel like avg(SNR), max(SNR) and std_rayleigh.

## Arguments definition
- **path** : path of the DICOM file to analyse
- **z_slice** : specify the slice to analyse
- **coil_name** : name of the particular coil used (for identification only)

The last part of the code is for plotting. Here is a list of the figures that are produced :

## Figures
- The mask of the noise region used to compute SNR
- The distribution of noise on an histogram for each of the chanel. It should be a Rayleigh distribution (ref)
- The SNR map for each of the channel

## Test run 
By changing the variable _path1_ and _path2_ to the paths corresponding to Wantcom and HiQ respectively and by selecting the 18th slice, one should produced these figures:

![mask_wantcom](https://github.com/CharlesPageot/SNR_calculation/assets/167803616/9df472f2-4d45-4ca5-bb76-d59ece17d086)

![mask_hiq](https://github.com/CharlesPageot/SNR_calculation/assets/167803616/3eb308ea-7012-4e25-8e83-28e542200848)

![noise_distr](https://github.com/CharlesPageot/SNR_calculation/assets/167803616/b08ee3a0-8913-4b0e-b39d-7d8f6e1c7aa4)

![SNR_maps](https://github.com/CharlesPageot/SNR_calculation/assets/167803616/e57a3595-68ff-46c4-9eea-e83e2cc66b5b)

