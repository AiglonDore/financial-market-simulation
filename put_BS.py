import numpy as np
from math import *
from random import *
import matplotlib.pyplot as plt
import scipy.stats as stats



def F (x) :
    return stats.norm.cdf(x)

def put_BS (s,r,sigma,T,K) :
    d1 = (1/(sigma*(T**(1/2))))*(np.log(s/K)+(r+(sigma**2)/2)*T)
    d2 = d1-sigma * (T**1/2)
    prix_BS = -s*F(-d1) + K*np.exp(-r*T)*F(-d2)
    return prix_BS
