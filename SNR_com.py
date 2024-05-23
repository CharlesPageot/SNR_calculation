import numpy as np
import nibabel as nib
from matplotlib import pyplot as plt
from scipy.stats import rayleigh
import matplotlib.patches as patches

path1 = '2024-05-16-data_coil\\_cohen-adad_coil_tests_20_20240514105048_4.nii'
path2 = '2024-05-16-data_coil\\_cohen-adad_coil_tests_20_20240514105048_12.nii'


def compute_SNR(path, z_slice, coil_name):

    print(f'{coil_name} :\n')

    nifti_img  = nib.load(path)
    nii_data = nifti_img.get_fdata()
    slice = nii_data[:,:,z_slice,:]

    SNR_matrix = np.zeros(slice.shape)
    fit_array = []
    noise_data = []

    mask = slice[:,:,-1] < 200

    plt.pcolormesh(mask)
    plt.title(f'Noise mask for {coil_name}')
    plt.show()

    for i in range(int(slice.shape[2])):

        # apply the mask on the image
        noise_vector = slice[:,:,i][mask]
        noise_data.append(noise_vector)

        # find the std_rayleigh and the fitting parameters for visualisation
        std = np.std(noise_vector)
        fit_params = rayleigh.fit(noise_vector)
        std_ray = np.sqrt(2-np.pi/2)*std
        fit_array.append([std_ray, fit_params])

        # SNR definition and info about each channel
        SNR_matrix[:,:,i] = slice[:,:,i]/std_ray
        max_SNR = np.max(SNR_matrix[:,:,i])
        avg_SNR = np.mean(SNR_matrix[:,:,i])

        print(f'CH {i+1} : max(SNR) = {max_SNR:.0f}, avg(SNR) = {avg_SNR:.0f} and std = {std_ray:.0f}')

    return noise_data, fit_array, SNR_matrix

noise_wantcom, fit_wantcom, SNR_wantcom = compute_SNR(path1, 18,'Wantcom')
noise_hiq, fit_hiq, SNR_hiq = compute_SNR(path2, 18, 'HiQ')

# plotting the statistical analysis

fig, axs = plt.subplots(2,5, figsize=(8, 3),constrained_layout=True, dpi=150)

for i in range(int(SNR_wantcom.shape[2])):
    fig.suptitle(f'Noise distributions for Wantcom (top) and HiQ (bottom)', fontweight="bold")

    if i == 4:
        x = np.linspace(0,400)

        loc, scale = fit_wantcom[i][1]
        noise_vector = noise_wantcom[i]
        axs[0,i].hist(noise_vector, density=True,bins=50)
        p = rayleigh.pdf(x, loc, scale)
        axs[0,i].plot(x, p, 'k', linewidth=2)
        axs[0,i].set_title('Combined')

        loc, scale = fit_hiq[i][1]
        noise_vector = noise_hiq[i]
        axs[1,i].hist(noise_vector, density=True,bins=50)
        p = rayleigh.pdf(x, loc, scale)
        axs[1,i].plot(x, p, 'k', linewidth=2)

    else:
        x = np.linspace(0,400)

        loc, scale = fit_wantcom[i][1]
        noise_vector = noise_wantcom[i]
        axs[0,i].hist(noise_vector, density=True,bins=50)
        p = rayleigh.pdf(x, loc, scale)
        axs[0,i].plot(x, p, 'k', linewidth=2)
        axs[0,i].set_title(f'Channel {i+1}')

        loc, scale = fit_hiq[i][1]
        noise_vector = noise_hiq[i]
        axs[1,i].hist(noise_vector, density=True,bins=50)
        p = rayleigh.pdf(x, loc, scale)
        axs[1,i].plot(x, p, 'k', linewidth=2)

# plt.tight_layout()
plt.show()

# plotting the SNR maps

if np.max(SNR_wantcom) > np.max(SNR_hiq):
    maximum = np.max(SNR_wantcom)
else:
    maximum = np.max(SNR_hiq)

fig, axs = plt.subplots(2,5,figsize=(8, 3), constrained_layout=True, dpi=150)
fig.suptitle(f'SNR maps for Wantcom (top) and HiQ (bottom)', fontweight="bold")

for i in range(int(SNR_wantcom.shape[2])):

    if i == 4:
        h = axs[0,i].pcolormesh(SNR_wantcom[::-1,:,i], vmin= 0, vmax=maximum)
        axs[0,i].set_title(f'Combined')
        axs[0,i].axis('off')

        h = axs[1,i].pcolormesh(SNR_hiq[::-1,:,i], vmin= 0, vmax=maximum)
        axs[1,i].axis('off')

    else:
        h = axs[0,i].pcolormesh(SNR_wantcom[::-1,:,i], vmin= 0, vmax=maximum)
        axs[0,i].set_title(f'Channel {i+1}')
        axs[0,i].axis('off')

        h = axs[1,i].pcolormesh(SNR_hiq[::-1,:,i], vmin= 0, vmax=maximum)
        axs[1,i].axis('off')

fig.colorbar(h, ax=axs.ravel().tolist())
plt.show()


