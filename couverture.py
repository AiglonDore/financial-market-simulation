import numpy as np
from premier_pricer import q_N


def couverture(N, r_N, h_N, b_N, s, f):
    qN = q_N(r_N, b_N, h_N)
    res = []
    a = []
    b = []
    s_t = []
    for k in range(0, N):
        e = s*(1+h_N)**(N-1-k)*(1+b_N)**k
        s_t.append(e)
    for elem in s_t:
        alpha = (f((1+h_N)*elem)-f((1+b_N)*elem))/((h_N-b_N)*elem)
        a.append(alpha)
        beta = ((1+h_N)*f((1+b_N)*elem)-(1+b_N) *
                f((1+h_N)*elem))/((h_N-b_N)*((1+r_N)**N))
        b.append(beta)
    res.append([a, b])
    i = N-1
    a = []
    b = []
    s_k = []
    for k in range(0, i):
        e = s*(1+h_N)**(i-1-k)*(1+b_N)**k
        s_k.append(e)
    for elem in s_k:

        v_h_N = (qN*f((1+h_N)*(1+h_N)*elem) + (1-qN)
                 * f((1+b_N)*(1+h_N)*elem))/(1+r_N)
        v_b_N = (qN*f((1+h_N)*(1+b_N)*elem) + (1-qN)
                    * f((1+b_N)*(1+b_N)*elem))/(1+r_N)

        alpha = (v_h_N - v_b_N)/((h_N-b_N)*elem)
        a.append(alpha)
        beta = ((1+h_N)*v_b_N-(1+b_N)*v_h_N)/((h_N-b_N)*((1+r_N)**i))
        b.append(beta)
    res.append([a, b])
    return res


def f1(x):
    return max(x-100, 0)

L=couverture(2, 0.03, 0.05, -0.05, 100, f1)
print("Couverture à la date 0:",(L[1][0][0],L[1][1][0]))
print("Couverture à la date 1:",(L[0][0],L[0][1]))