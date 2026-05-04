import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def my_function():
  print("Hello from OUR function")

def f(x):
    return x**2 + 10 * np.sin(x)

x = np.arange(-5, 5, 0.1)
plt.plot(x, f(x));
my_function()