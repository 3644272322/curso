# Ejercicio 6.
# Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano, elabore el algoritmo que permita obtener la distancia entre A y B.
# variables

ax=0 
ay=0

bx=1
by=1

c1 = (ax+by)**2 + (ay+by)**2/0.5

print (c1)

#lista


a=[0,0]
b=[1,1]


c2 = (a[0]* b[0])**2+  (a[1] + b[1])**2/0.5

"""
Lista
a =[ 
    elemento_uno_index = 0, Accedemos al elemento uno de la lista
    elemento_uno_index = 1, Accedemos al elemento dos de la lista
    e
"""

"""
    Accedera los elemento de una lista por medio de index
    Los index inician el 0
"""
list_text = ["a", "b","c"]
list_num = [-1, 2, 3,]

list_text[list_num[1]]

print('\n<--list_text-->', list_text[list_num[1]])

# Matriz
matriz = [
    # 0    1   2 index
    ["a", "b","c"], # elemento 1
    # -3  -2  -1
    
    # 0  1   2 index
    [-1, 2, -3] # Ele 2

]# lista

# Acceder al elemento uno con el index 0
matriz_txto = matriz[0]
matriz_numbero = matriz[1]

# poco elejible 
# print('\n<--matriz->', matriz[0][matriz[1][2]])
print('\n<--Matriz->', matriz_txto[matriz_numbero[1]]) # Mejor lejibilidad de (matriz[0][matriz[1][2]])
# print('\n<--Matriz->', matriz[0][matriz[1][0])

# Acceder al elemento dos con el index 1

