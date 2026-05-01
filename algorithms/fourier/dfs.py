import numpy as np


def discrete_fourier_series(f):
    """
    Discrete Fourier Series (DFS)

    Parameters
    ----------
    f : ndarray
        One period of a discrete-time periodic signal (length N)

    Returns
    -------
    c : ndarray
        DFS coefficients
    """
    N = len(f)
    n = np.arange(N)    # n: frequency index
    k = np.arange(N)    # k: time index

    exponent = np.exp(-1j * 2 * np.pi * np.outer(n, k) / N)
    c = (1 / N) * np.dot(exponent, f)

    return c


def inverse_dfs(c, k):
    """
    Inverse DFS

    Parameters
    ----------
    c : ndarray
        DFS coefficients
    k : ndarray
        Time index

    Returns
    -------
    fn : ndarray
        Reconstructed signal
    """

    N = len(c)

    n = np.arange(N)    # n: frequency index

    exponent = np.exp(1j * 2 * np.pi * np.outer(k, n) / N)
    f = np.dot(exponent, c)

    return f