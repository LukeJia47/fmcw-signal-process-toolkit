import numpy as np

from algorithms.fourier.dft import discrete_fourier_transform

def fast_fourier_transform(f):
    """
    Fast Fourier Transform (FFT) using radix-2 Cooley-Tukey algorithm

    Parameters
    ----------
    f : np.ndarray
        Input signal (1D array)

    Returns
    -------
    F : np.ndarray
        Complex FFT spectrum (same length as input)

    """

    # ensure input is numpy array
    f = np.asarray(f)

    N = len(f)

    # handle empty input
    if N == 0:
        return np.array([])

    # check if N is power of 2
    if (N & (N - 1)) == 0:
        # base case
        if N == 1:
            return f
        else:
            # compute twiddle factors
            n = np.arange(N // 2)
            Wn = np.exp(-1j * 2 * np.pi * n / N)

            # split into even and odd indices
            x_even = f[0::2]
            x_odd = f[1::2]

            # recursive FFT
            Xe = fast_fourier_transform(x_even)
            Xo = fast_fourier_transform(x_odd)

            # combine results
            twiddle = Wn * Xo

            return np.concatenate([Xe + twiddle, Xe - twiddle])

    else:
        # fallback to O(N^2) DFT if N is not a power of 2
        return discrete_fourier_transform(f)