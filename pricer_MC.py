import numpy as np
from math import *
from random import *
import matplotlib.pyplot as plt
import scipy.stats as stats

def pricer_MC (n,s,r,sigma,T,f) :
    epsilon = np.random.normal(0,1,n) # a faire plus tard il faut une liste de n va indépendante et iid de loi N(0,1)
    somme = 0
    for i in range (1, n+1) :
        val = s*exp((r-(sigma**2)/2)*T+sigma*(T**(1/2))*epsilon[i-1])
        somme = somme + f(val)
    return (exp(-r*T)/n)*somme

def F (x) :
    return stats.norm.cdf(x)

def put_BS (s,r,sigma,T,K) :
    d1 = (1/(sigma*(T**(1/2))))*(log(s/K)+(r+(sigma**2)/2)*T)
    d2 = d1-sigma * (T**(1/2))
    prix_BS = -s*F(-d1) + K*exp(-r*T)*F(-d2)
    return prix_BS

Y=[]
Z=[]
for k in range(1,11):
    n=k * 10 ** 5
    f=lambda x:max(90-x,0)
    Y.append(pricer_MC(n,100,0.01,0.1,1,f))
    Z.append(put_BS(100,0.01,0.1,1,90))


plt.plot(range(1,11),Y,Z)
plt.show()