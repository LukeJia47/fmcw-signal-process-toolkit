import numpy as np

def discrete_fourier_transform(f):
    """
    Naive Discrete Fourier Transform (O(N^2))

    Parameters
    ----------
    f: np.array
        Input signal

    Returns
    -------
    F: np.array
        DFT spectrum

    """
    N = len(f)

    k = np.arange(N)    # time index
    n = np.arange(N)    # frequency index

    exponent = np.exp(-1j * 2 * np.pi * np.outer(n,k)/N)
    F = np.dot(exponent, f)

    return F