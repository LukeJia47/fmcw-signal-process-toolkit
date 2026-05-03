import numpy as np

def ca_cfar(x, Tr = 8, Td = 4, Gr = 4, Gd = 2, offset = 6):
    """
    2D Cell-Averaging CFAR (CA-CFAR)

    Parameters
    ----------
    x : np.ndarray
        Input Range-Doppler map
    Tr : int
        Number of training cells in range dimension
    Td : int
        Number of training cells in Doppler dimension
    Gr : int
        Number of guard cells in range dimension

    Gd  : int
        Number of guard cells in Doppler dimension
    offset   : float
        Threshold offset in dB (advice: 5 ~15)

    Returns
    -------
     detection : np.ndarray
        Binary detection map (same shape as input)

    """

    [Nr, Nd] = x.shape

    detection = np.zeros_like(x, dtype=np.uint8)

    # number of training cells
    total_cells = (2 * (Tr + Gr) + 1) * (2 * (Td + Gd) + 1)
    guard_cells = (2 * Gr + 1) * (2 * Gd + 1)
    N_train = total_cells - guard_cells

    for i in range(Tr+Gr, Nr - (Gr+Tr)):
        for j in range(Td+Gd, Nd - (Gd+Td)):

            noise_level = 0.0

            for p in range(i - (Tr+Gr), i + (Tr+Gr) + 1):
                for q in range(j - (Gd+Td), j + (Gd+Td) + 1):

                    # exclude guard cells
                    if abs(i - p) > Gr or abs(j - q) > Gd:
                        noise_level =  noise_level + x[p,q]

            # average noise (linear)
            noise_level = noise_level / N_train
            threshold = noise_level

            # add offset
            threshold *= offset

            # CUT
            if x[i,j] > threshold:
                detection[i,j] = 1


    return detection

