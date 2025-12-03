import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as npl


def main():
    zad4()


def zad1():
    a = pow(3, 12) - 5
    print(a)
    b = (
        np.array([[2, 0.5]])
        * np.array([[1, 4], [-1, 3]])
        * np.array([[-1, -3]]).transpose()
    )
    print(b)
    c = npl.matrix_rank(np.array([[1, -2, 0], [-2, 4, 0], [2, -1, 7]]))
    print(c)
    d = npl.inv(np.array([[1, 2], [-1, 0]])) * np.array([[-1, 2]])
    print(d)


def zad2():
    arr = np.array([1, 1, -129, 171, 1620])
    p = np.poly1d(arr)
    print(f"Wartosc w x=-46: {p(-46)}")
    print(f"Wartosc w x=14: {p(14)}")

    # zad 3.1 3.2
    step = 0.1
    var = np.arange(-46, 14, step)
    varp = p(var)
    print(f"max: {max(varp)}")
    print(f"min: {min(varp)}")


def zad4():
    arr = np.array([1, 1, -129, 171, 1620])
    p = buildpoly(arr)
    anylyzepoly(p, -46, 14, 0.1)


def buildpoly(coef):
    return np.poly1d(coef)


def anylyzepoly(polynomial, rangeMin, rangeMax, accuracy):
    range = np.arange(rangeMin, rangeMax, accuracy)
    var = polynomial(range)
    print(f"Stopien wielomianu: {polynomial.order}")
    maxv = max(var)
    minv = min(var)
    print(f"max: {maxv}")
    print(f"min: {minv}")

    imax = np.argmax(var)
    imin = np.argmin(var)

    # zad5
    plt.figure()
    plt.plot(range, var)
    plt.title("wartosci wielomianu")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.scatter(range[imax], maxv, c="red", label="max")
    plt.scatter(range[imin], minv, c="green", label="min")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
