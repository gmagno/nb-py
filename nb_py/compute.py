
import numpy as np

def compute(
    imw=128, imh=128,
    coefs=[1, 0, 0, 0, 0, 0, 1],
    crmin=-5.0, crmax=5.0,
    cimin=-5.0, cimax=5.0,
    itmax=30, tol=1e-6,
):
    '''
    Computes a Newton Basins image of `imh`-by-`imw`-by-3 pixels. The polynomial
    coefficients are passed in the form of a list in `coefs`. The image is
    constrained, in complex plane, to the rectangle area specified by (`crmin`,
    `cimin`) in the lower left corner, and (`crmax`, `cimax`) in the upper right
    corner. The algorithm has a maximum number of iteration `itmax` to converge a
    root, and a tolerance of `tol` is used as criterion of convergence.

    Returns a numpy ndarray of rows-by-cols-by-3 in HSV (hue, saturation,
    value) color format.
    '''
    roots = np.roots(coefs)
    hsv_array = np.zeros((imh, imw, 3), dtype=np.float32)
    for idx, _ in np.ndenumerate(hsv_array[:, :, 0]):
        y, x = idx
        r = crmin + (crmax - crmin) / imw * x
        i = cimax - (cimax - cimin) / imh * y
        z = complex(r, i)
        k = 0
        while k < itmax:
            f = np.polyval(coefs, z)
            df = np.polyval(np.polyder(coefs), z)
            if df != 0.0:
                z = z - f/df
                f_curr = np.polyval(coefs, z)
                if np.absolute(f_curr) <= tol:
                    root = np.abs(roots - z).argmin()
                    h = root/roots.size
                    s = 1
                    v = 1 - k / itmax
                    hsv_array[y, x] = np.asarray([h, s, v])
                    break
            k += 1

    return hsv_array
