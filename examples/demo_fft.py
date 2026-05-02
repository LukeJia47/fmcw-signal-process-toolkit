import numpy as np
import matplotlib.pyplot as plt

from algorithms.fourier.fft import fast_fourier_transform

def main():
    # fundamental period (seconds)
    T = 1 / 50

    # number of samples per period
    N = 128

    # sampling period
    Ts = T / N

    # signal frequencies (Hz), must be below Nyquist frequency
    freq1 = 500
    freq2 = 1000

    # time index
    k = np.arange(N)

    # discrete-time periodic signal (one period)
    signal = 1 / 2 + 2 * np.sin(2 * np.pi * freq1 * k * Ts) + np.sin(2 * np.pi * freq2 * k * Ts)

    # FFT
    F = fast_fourier_transform(signal)

    # amplitude spectrum
    A = np.abs(F) / N

    # frequency axis (Hz)
    fs = 1 / Ts
    freq = np.arange(N // 2 + 1) * fs / N

    Ap = A[:N // 2 + 1]
    if N % 2 == 0:
        Ap[1:-1] *= 2  # DC and Nyquist excluded
    else:
        Ap[1:] *= 2

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(k, signal)
    plt.xlabel('Time index')
    plt.ylabel('Signal')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(freq, Ap)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()