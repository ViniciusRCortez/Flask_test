import numpy as np
import matplotlib.pyplot as plt


def teste():
    x = np.arange(0, 10, 1)
    y = 3*x

    plt.plot(x, y)
    plt.savefig(r'static\teste.png')


teste()
