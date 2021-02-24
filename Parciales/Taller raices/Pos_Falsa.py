import numpy as np
import math

# INGRESO
fx = lambda x: (math.cos(x)*2)-x*2

a = 0
b = 1
tolerancia = 0.000000000000000000000000001

# PROCEDIMIENTO
tabla = []
tramo = abs(b-a)
fa = fx(a)
fb = fx(b)

while not(tramo<=tolerancia):
    
    c = b - fb*(a-b)/(fa-fb)
    fc = fx(c)
    cambio = np.sign(fa)*np.sign(fc)
    tabla.append([a,c,b,fa,fc,fb,tramo])
    
    if cambio>0:
        tramo = abs(c-a)
        a = c
        fa = fc
    else:
        tramo = abs(b-c)
        b = c
        fb = fc
    

tabla = np.array(tabla)
ntabla = len(tabla)
# SALIDA
for i in range(0,ntabla,1):
    print('iteración:  ',i)
    

print('raiz:  ',c)
print('error: ',tramo)