import numpy as np
from matplotlib import pyplot as plt
from algorithms.detection.cfar import  ca_cfar

if __name__ == '__main__':
    """
    Radar specifications
    Carrier frequency: 77 GHz
    Max range: 200 m
    Range resolution: 1 m
    """
    fc = 77e9
    R_max = 200
    R_res = 1

    c = 3e8

    """
    Target definition (constant velocity)
    Initial range: 110 m
    Velocity: -20 m/s
    """
    target_r = 110
    target_v = -20

    """
    FMCW waveform design
    Compute bandwidth B, chirp time Tc, and slope S
    Tc is chosen as ~5.5 times round-trip time
    """
    B = c / (2 * R_res)
    Tc = (5.5 * 2 * R_max) / c
    S = B / Tc

    # Number of chirps (Doppler dimension)
    Nd = 128

    # Number of samples per chirp (Range dimension)
    Nr = 1024

    # Time vector

    # sampling time
    fast = np.linspace(0, Tc, Nr, endpoint=False)
    slow = np.arange(Nd) * Tc
    t_fast = fast[:, None]
    t_slow = slow[None, :]

    t = t_fast + t_slow

    # Target range and delay
    r_t = target_r + target_v * t_slow  # ❗只随slow time变化
    td = 2 * r_t / c

    """
    Signal generation
    """
    Tx = np.cos(2 * np.pi * (fc * t + 0.5 * S * t ** 2))
    Rx = np.cos(2 * np.pi * (fc * (t - td) + 0.5 * S * (t - td) ** 2))

    sig = Tx * Rx
    sig = sig.reshape(Nr, Nd)

    """
    Range-Doppler Map (2D FFT)
    """
    range_window = np.hanning(Nr).reshape(-1,1)
    doppler_window = np.hanning(Nd).reshape(1,-1)
    window_2d = range_window * doppler_window
    sig_windowed = sig * window_2d

    sig_fft = np.fft.fft(sig_windowed, axis=0)   # range
    sig_fft = np.fft.fft(sig_fft, axis=1) # doppler
    sig_fft = sig_fft / (Nr * Nd)
    sig_fft = sig_fft[:Nr // 2, :Nd]
    sig_fft = np.fft.fftshift(sig_fft, axes=1)

    RDM = np.abs(sig_fft)**2
    RDM_cf = RDM
    RDM_dB = 10 * np.log10(RDM / np.max(RDM))

    # Axes
    lambda_c = c / fc
    fd = np.arange(-Nd // 2, Nd // 2) / (Nd * Tc)
    velocity_axis = fd * lambda_c / 2

    range_axis = np.arange(Nr // 2) * (c / (2 * B))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    D, R = np.meshgrid(velocity_axis, range_axis)
    ax.plot_surface(D, R, RDM_dB, cmap='viridis')

    ax.set_xlabel('Doppler')
    ax.set_ylabel('Range')
    ax.set_zlabel('RDM')
    ax.set_title('2D FFT')

    """
    CFAR detection
    """
    Detect = ca_cfar(RDM_cf,Tr=6,Td=3,Gr=1,Gd=1,offset=10)

    fig = plt.figure('CFAR Detection')
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(D, R, Detect, cmap='viridis')
    fig.colorbar(surf)

    ax.set_xlabel('Doppler')
    ax.set_ylabel('Range')
    ax.set_title('CFAR Detection')

    plt.show()

