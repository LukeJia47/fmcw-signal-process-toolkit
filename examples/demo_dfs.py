import numpy as np
import matplotlib.pyplot as plt

from algorithms.fourier.dfs import discrete_fourier_series, inverse_dfs

def extend_frequency_index(c, N, periods=5):
    """
    Extend DFS coefficients for visualization
    """
    n_ext = np.arange(-periods * N, periods * N)

    c_ext = c[n_ext % N]

    return c_ext, n_ext

def main():
    # periodic signal
    f = np.array([1, 1, 0, 0])
    # Period length
    N = 4

    # specturm
    c = discrete_fourier_series(f)

    # evaluate DFS inverse over extended time indices (±5N samples)
    k = np.arange(-N*5, N*5)

    # reconstructed_signal
    f_rec = inverse_dfs(c,k)

    # Note: DFS spectrum is periodic; extension is for visualization only
    [c_ext, n_ext] = extend_frequency_index(c, N)

    # 时域
    plt.figure()
    plt.stem(k, f_rec.real)
    plt.title("Reconstructed Periodic Signal (DFS inverse)")

    # 频域
    plt.figure()
    plt.stem(n_ext, c_ext.real)
    plt.title("DFS Coefficients")

    plt.show()


if __name__ == "__main__":
    main()