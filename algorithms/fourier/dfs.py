import numpy as np


def discrete_fourier_series(f, N):
    """
    Discrete Fourier Series (DFS)

    Parameters
    ----------
    f : ndarray
        One period of the signal
    N : int
        Period length

    Returns
    -------
    c : ndarray
        DFS coefficients
    """
    n = np.arange(N)
    c = np.zeros(N, dtype=complex)

    for k in range(N):
        c[k] = (1 / N) * np.sum(f * np.exp(-1j * 2 * np.pi * k * n / N))

    return c


def inverse_dfs(c, k_range):
    """
    Inverse DFS

    Parameters
    ----------
    c : ndarray
        DFS coefficients
    k_range : ndarray
        Time index

    Returns
    -------
    fn : ndarray
        Reconstructed signal
    """
    N = len(c)
    fn = np.zeros(len(k_range), dtype=complex)

    for k in range(N):
        fn += c[k] * np.exp(1j * 2 * np.pi * k * k_range / N)

    return fn
