# -*- coding: utf-8 -*-
"""Matriz triangular inferior"""

#Transformando M1 em uma matriz triangular inferior, atribuindo zero a todos os elementos acima da diagonal principal.
#M1
import numpy as np
def triangular_inferior(m1):
  for linha in range(3):
    for coluna in range(3):
      if(linha < coluna):
        m1[linha][coluna] = 0
  return m1

m1 = np.array([[1, 2, 3], [5, 6, 7], [8, 9, 0]])
m2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(triangular_inferior(m1))
print("\n",m2)
