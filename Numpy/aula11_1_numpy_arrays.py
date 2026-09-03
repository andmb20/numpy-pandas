# Continuando criação de Arrays

# Random - rand, randn e randint
# rand() - Gera números aleatórios entre 0 e 1, com distribuição uniforme.
# randn() - Gera números aleatórios decimais, mas seguindo uma distribuição normal (gaussiana), centrada em 0.
# randint() - Gera números inteiros aleatórios dentro de um intervalo.

import numpy as np

# print(np.random.rand(10)) output: [0.10585206 0.51647701 0.83032687 0.51768951 0.04190108 0.63534231 0.12239705 0.1295682  0.9151387  0.89717925]
# print(np.random.randn(10)) output: [ 1.51848409 -1.1052892   1.26017717 -0.32086324  0.20178704 -1.24642337  0.49993856  0.33876263  0.23642304 -1.14681768]
# print(np.random.randint(10,100,30)) output: [55 42 66 84 98 94 14 56 80 38 64 40 98 47 82 55 99 38 93 61 80 67 22 67 26 62 60 66 83 63]

# Arrays unidimensional: [55 42 66 84 98 94 14 56 80 38 64 40 98 47 82 55 99 38 93 61 80 67 22 67 26 62 60 66 83 63]
# Exemplo: Arrays bidimensional 
array_bidimensional_zeros = np.zeros((5,4)) # output : Verificado com dois colchetes [[ no inicio     ]] no final ; 5 = linhas ; 4 = colunas
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

array_bidimensional_ones = np.ones((5,4)) # output : 5 = linhas ; 4 = colunas
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

array_bidimensional_eye = np.eye(6) # output : observe o número 1 dentro do array = é uma matriz identidade
# [[1. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0.]
#  [0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 1. 0. 0.]
#  [0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 1.]]

print(array_bidimensional_eye)