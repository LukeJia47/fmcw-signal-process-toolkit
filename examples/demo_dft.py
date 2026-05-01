import numpy as np
import matplotlib.pyplot as plt
import math

from algorithms.fourier.dft import discrete_fourier_transform

def main():
    # a discrete-time periodic signal
    T = 1/50    # fundamental period (s)
    N = 100     # number of samples per period
    Ts = T/N    # sampling period

    # Signal frequencies are chosen below Nyquist limit
    freq1 = 500
    freq2 = 1000

    k = np.arange(N)    # time index

    # discrete-time signal
    signal = 0.5 + 2*np.sin(2*np.pi*freq1*k*Ts) + np.sin(2*np.pi*freq2*k*Ts)

    # DFT
    FN = discrete_fourier_transform(signal)
    A = np.abs(FN)   # magnitude spectrum

    # single-sided spectrum
    Ap_num = N // 2 + 1

    Ap = A[:Ap_num] / N
    if N % 2 == 0:
        Ap[1:-1] *= 2  # DC and Nyquist excluded
    else:
        Ap[1:] *= 2

    fp = np.arange(Ap_num) * (1 / (N * Ts))

    plt.figure()
    plt.subplot(3, 1, 1)
    plt.plot(k, signal)
    plt.xlabel('Time index')
    plt.ylabel('signal')
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(np.arange(N), A)
    plt.xlabel('Frequency bin index')
    plt.ylabel('Magnitude')
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(fp, Ap)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()


