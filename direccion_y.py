import numpy as np
from solve import *

r = np.array([[0],
              [1],
              [0]])

def normalizar_phi (phi):
    return phi * (phi.T @ M @ r)*(phi.T @ M @ phi)**(-1)

phi_1_norm = normalizar_phi(phi1)
phi_2_norm = normalizar_phi(phi2)
phi_3_norm = normalizar_phi(phi3)

print("phi_1_norm:", phi_1_norm)
print("phi_2_norm:", phi_2_norm)
print("phi_3_norm:", phi_3_norm)
#Ademas, la matriiz de vectores propios normalizados es:
Phi = np.array([phi_1_norm, phi_2_norm, phi_3_norm]).T

def normalizar_matriz (matriz):
    return Phi.T @ matriz @ Phi

Mm = normalizar_matriz(M)
km = normalizar_matriz(K)

Meff1 = Mm[0, 0]
Meff2 = Mm[1, 1]
Meff3 = Mm[2, 2]

def frac (meff):
    return meff * (r.T @ M @ r)**(-1)

frac1 = frac(Meff1)
frac2 = frac(Meff2)
frac3 = frac(Meff3)

print("Meff1:", Meff1)
print("Meff2:", Meff2)
print("Meff3:", Meff3)

print("frac1:", frac1)
print("frac2:", frac2)
print("frac3:", frac3)