import numpy as np
from datos import *

#Defino un k inicial
k = 1

#En primer lugar defino las matrices K y M

K = np.array([[3*k, 0, -10*k], 
               [0, 3*k, 0],
               [-10*k, 0, 100*k]])

M = np.array([[mu*b*h, 0, 0],
               [0, mu*b*h, 0],
               [0, 0, (mu*b*h*(b**2 + h**2))/12]])

#Luego los valores propios son:
valores_propios, vectores_propios = np.linalg.eig(np.linalg.inv(M) @ K)

valores_propios = np.sqrt(valores_propios)

min_valor = np.min(valores_propios) #Es el omega que hace el perido mas largo

k = (2 * np.pi/ (min_valor * T1))**2 #Lo paso a radianes por segundo

#Por lo tanto, los nuevos valores y vectores propios son:

valores_propios, vectores_propios = np.linalg.eig(np.linalg.inv(M) @ (K + k * M))
valores_propios = np.sqrt(valores_propios)

#Ahora normalizo los vectores propios
phi1, phi2, phi3 = vectores_propios[:, 0], vectores_propios[:, 1], vectores_propios[:, 2]












