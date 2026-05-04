"""Do some fun stuff"""

import numpy as np  # pylint: disable=import-error
import matplotlib.pyplot as plt  # pylint: disable=import-error


def my_function():
    """Say hello"""
    print("Hello from my function")


def f(a):
    """Calculate some wack shit"""
    return a**2 + 10 * np.sin(a)


if __name__ == "__main__":
    x = np.arange(-5, 5, 0.1)
    plt.plot(x, f(x))
    my_function()
