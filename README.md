# SNR_calculation

Python script to analyse the signal-to-noise-ratio (SNR) from a recontructed DICOM file. The main function **SNR_compute** read the file, analyse the image and produce figures about the SNR.

## Arguments definition
- **path** : path of the DICOM file to analyse
- **z_slice** : specify the slice to analyse
- **coil_name** : name of the particular coil used (for identification only)

## Figures produced
- The mask of the noise region used to compute SNR
- The distribution of noise on an histogram for each of the chanel. It should be a Rayleigh distribution (ref)
- The SNR map for each of the channel

## Test run 
By changing the variable _path1_ to the path corresponding to the Wantcom coil and by selecting the 18th 
