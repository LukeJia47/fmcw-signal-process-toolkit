import numpy as np
import matplotlib.pyplot as plt

from algorithms.fourier.dfs import discrete_fourier_series, inverse_dfs


def main():
    # 周期信号
    f = np.array([1, 1, 0, 0])
    N = 4

    k = np.arange(-20, 21)

    c = discrete_fourier_series(f, N)
    fn = inverse_dfs(c, k)

    # 时域
    plt.figure()
    plt.stem(k, fn.real)
    plt.title("Discrete Signal")

    # 频域
    plt.figure()
    plt.stem(np.arange(N), c.real)
    plt.title("DFS Coefficients")

    plt.show()


if __name__ == "__main__":
    main()
