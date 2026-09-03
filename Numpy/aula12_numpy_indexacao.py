import numpy as np

arr = np.arange(1,11,dtype=int) # output : [ 1  2  3  4  5  6  7  8  9 10]

#Indexação de Arrays
# print(arr[4]) : 5 
# print(arr[2:4]) : [3 4] = Eu quero o indice 2 até o indice 4 ( obs. não inclui o indice 4)
# print(arr[2:5]) : [3 4 5]
# print(arr[:5]) : [1 2 3 4 5] = do início até antes do índice 5
# print(arr[3:]) : [ 4  5  6  7  8  9 10] = Eu quero todos a partir do 3º indice
# print(arr[:]) : [ 1  2  3  4  5  6  7  8  9 10] = array inteiro 

# Indexação de Arrays Bidimensionais
arr2 = np.random.randint(10,50,size=(3,3)) # Primeiro valor do size representa a quantidade de linhas, Segundo valor do size representa a quantidade de colunas
# print(arr2[1][2]) Retorna o valor que está na linha 1 e coluna 2
# print(arr2[0][1:]) Retorna os valores que estão na linha 0 (lembrando que arrays salvam os index na sequencia 0,1,2.....) e indices da coluna 1 em diante 

arr3 = np.random.randint(1,101,size=(10,10))
# print(arr3[2,3]) Retorna o valor que está na linha 2 e coluna 3 / Essa é outra maneira de retornar valores de um array com [,] e não dois [][]
# print(arr3[0:2,7:10]) Retorna os valores que estão nas linhas 0 e 1 e nas colunas 7, 8 e 9
# print(arr3[6:,7:]) Retorna os valores a partir da linha 6 e coluna 7
# print(arr[[8,5,6]]) Retorna as linhas com os indices 8,5,6 exatamente nessa sequencia