def fact(n):
    if n==0:
        return(1)
    else:
        f=1
        for k in range(1, n+1):
            f=f*k
        return(f)

def coeff_binomiaux(k, n):
    return((fact(n))/(fact(k)*fact(n-k)))

def q_N(r_N, b_N, h_N):  #calcul de q_n grâce à la formule de la question 1
    return((r_N-b_N)/(h_N-b_N))

def pricer_1(N, r_N, h_N, b_N, s, f): #calcul du prix de l'option selon la formule de la question 2
    esperance = 0 #contiendra l'espérance de f(Stn)
    proba = 0
    pay_off = 0
    for k in range(0, N+1):
        proba = coeff_binomiaux(k, N)*((q_N(r_N, b_N, h_N))**k)*((1-q_N(r_N, b_N, h_N))**(N-k))
        pay_off = f(s*((1+h_N)**k)*((1+b_N)**(N-k)))
        esperance += pay_off*proba
    res = 1/((1+r_N)**N)*esperance
    return(res)

def f(x):
    return(max(x-110,0))

print(pricer_1(20, 0.02, 0.05, -0.05, 100, f))