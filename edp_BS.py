import numpy as np
from math import *
import matplotlib.pyplot as plt
import scipy.linalg

def p_t_x_min(K, T, M, r, x_min, m):
    delta_T = T/M
    return(K*exp(-r*m*delta_T)-exp(x_min))

def theta_fonction(theta, K, r, sigma, T, x_min, x_max, N, M):
    h = (x_max - x_min)/N
    delta_t = T/M
    A = -(theta*sigma**2)/(2*h**2) + (r-(sigma**2)/(2))*((theta)/(2*h))
    B = -(1)/(delta_t) + (theta*sigma**2)/(h**2) + r
    C = -(theta*sigma**2)/(2*h**2) - (r-(sigma**2)/(2))*((theta)/(2*h))
    D = -((1-theta)*sigma**2)/(2*h**2) + (r-(sigma**2)/(2))*((1-theta)/(2*h))
    E = (1)/(delta_t) + ((1-theta)*sigma**2)/(h**2)
    F = -((1-theta)*sigma**2)/(2*h**2) - (r-(sigma**2)/(2))*((1-theta)/(2*h))
    U = np.zeros((N-1,N-1))
    V = np.zeros((N-1,N-1))
    W = np.zeros((N-1,1))
    P = np.zeros((N-1,1))

    for i in range(0, N-1):
        P[i,0] = max(0, K - exp(x_min + (i+1)*h))
        U[i,i] = E
        V[i,i] = -B
        if i>0:
            U[i,i-1] = D
            V[i,i-1] = -A
        if i<N-2:
            U[i,i+1] = F
            V[i,i+1] = -C

    (Z,l,u) = scipy.linalg.lu(U)

    for m in range(0, M):
        W[0,0] = -D*p_t_x_min(K, T, M, r, x_min, m+1)-A*p_t_x_min(K, T, M, r, x_min, m)
        X = np.dot(V, P) + W
        Y = np.linalg.solve(l, X)
        P = np.linalg.solve(u, Y)

    return P

X = theta_fonction(1, 0.9, 0.015, 0.21, 1, log(0.4), log(2), 100, 100)
Y = theta_fonction(0, 0.9, 0.015, 0.21, 1, log(0.4), log(2), 100, 100)
Z = theta_fonction(0.5, 0.9, 0.015, 0.21, 1, log(0.4), log(2), 100, 100)
W = np.linspace(log(0.4),log(2),99)

plt.plot(W,X)
plt.show()