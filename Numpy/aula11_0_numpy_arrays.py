# Biblioteca de Álgebra Linear para Python baseado em arrays

import numpy as np

# Transformar uma lista em um Array

qtde = [2,5,10,20,35]
custo = [100,150,450,320,195]

arr1 = np.array(qtde)
arr2 = np.array(custo)

# print(arr1) [ 2  5 10 20 35]
# print(arr2) [100 150 450 320 195]

# estoque = qtde * custo -> output: TypeError: can't multiply sequence by non-int of type 'list'

estoque = arr1 * arr2
# print(estoque) output: [ 200  750 4500 6400 6825]

custo = [100, 200, 300, 400]
venda = [125, 235, 355, 470]
arr3 = np.array(custo)
arr4 = np.array(venda)
lucro = arr4 - arr3
# print(lucro) output: [25 35 55 70]

# Arrays a partir do NumPy

# arange() → define o passo

# print(np.arange(10,20)) # output: [10 11 12 13 14 15 16 17 18 19]
# print(np.arange(10,20,2)) # output: [10 12 14 16 18]

# dtype significa, basicamente: qual será o tipo dos dados armazenados no array.
# print(np.arange(10,30,2, dtype=float)) # output: [10. 12. 14. 16. 18. 20. 22. 24. 26. 28.]

# linspace() → define a quantidade de valores

# print(np.linspace(0,1,10)) output: [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556 0.66666667 0.77777778 0.88888889 1.        ]
# print(np.linspace(1,10,30)) output: [ 1.          1.31034483  1.62068966  1.93103448  2.24137931  2.55172414  2.86206897  3.17241379  3.48275862  3.79310345  4.10344828  4.4137931  4.72413793  5.03448276  5.34482759  5.65517241  5.96551724  6.27586207  6.5862069   6.89655172  7.20689655  7.51724138  7.82758621  8.13793103  8.44827586  8.75862069  9.06896552  9.37931034  9.68965517 10.        ]