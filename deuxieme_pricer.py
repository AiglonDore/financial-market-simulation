import numpy as np
from premier_pricer import f, q_N


def pricer_2(N, r_N, h_N, b_N, s, f):
    qN = q_N(r_N, b_N, h_N)
    l1 = []
    for k in range(0, N+1):
        e = f(s*(1+h_N)**(N-k)*(1+b_N)**k)
        l1.append(e)
    for n in range(N, 0, -1):
        l2 = []
        for k in range(0, n):
            e = (l1[k]*qN + l1[k+1]*(1-qN))/(1+r_N)
            l2.append(e)
        l1 = l2
    return l1[0]


def f1(x):
    return max(x-100, 0)


print(pricer_2(3, 0.02, 0.05, -0.05, 100, f1))
