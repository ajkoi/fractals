import numpy as np
import matplotlib.pyplot as plt


def stability(c, z=0,  max_iter=20, horizon=2):
    for i in range(max_iter):
        z=z**2+c
        if abs(z)>=horizon:
            return i/max_iter
    return i/max_iter


def afficher(largeur=3, centre : complex = complex(-0.75, 0), resol=512, max_iter=20, horizon=2):
    scale = largeur/resol
    offset = -centre + complex(largeur, largeur)/2
    tab = [[0 for _ in range(resol)] for _ in range(resol)]
    X = []
    Y = []
    for i in range(len(tab)):

        for j in range(len(tab[i])):
            x = j*scale - offset.real
            y = i*scale - offset.imag
            tab[i][j] = stability(c=complex(x, y), max_iter=max_iter, horizon=horizon)
    X, Y = np.linspace(-offset.real, resol*scale-offset.real, resol), np.linspace(-offset.imag, resol*scale-offset.imag, resol)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pcolormesh(X, Y, tab)
    # plt.savefig("mand.png")
    plt.show()
def julia(c : complex,largeur=3, centre : complex = complex(-0.75, 0), resol=512, max_iter=20, horizon=2):
    scale = largeur/resol
    offset = -centre + complex(largeur, largeur)/2
    tab = [[0 for _ in range(resol)] for _ in range(resol)]
    X = []
    Y = []
    for i in range(len(tab)):

        for j in range(len(tab[i])):
            x = j*scale - offset.real
            y = i*scale - offset.imag
            tab[i][j] = stability(c=c, z=complex(x, y), max_iter=max_iter, horizon=horizon)
    X, Y = np.linspace(-offset.real, resol*scale-offset.real, resol), np.linspace(-offset.imag, resol*scale-offset.imag, resol)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pcolormesh(X, Y, tab)
    # plt.savefig("mand.png")
    plt.show()
