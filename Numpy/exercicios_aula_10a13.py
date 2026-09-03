# Exercícios com GPT

# Exercício 1/5 — Indexação e slicing

# Crie um array chamado arr contendo os números de 10 até 20.

# Depois, faça:

# Mostre o elemento que está no índice 4.
# Mostre os elementos dos índices 2 até 6, lembrando que o índice final do slicing não é incluído.
# Mostre todos os elementos a partir do índice 7.

import numpy as np

arr = np.arange(10,21)

print(arr[4])
print(arr[2:7])
print(arr[7:])

# Exercício 2/5 — Array 2D

# Crie um array matriz de 4 linhas e 5 colunas, contendo números inteiros aleatórios entre 1 e 50.

# Depois:

# Mostre o valor da linha 2, coluna 3.
# Mostre todas as colunas a partir da coluna 2, mas somente da linha 1.
# Mostre as linhas 0 e 1 e as colunas 3 e 4.

import numpy as np

arrmatriz = np.random.randint(1,51,size=(4,5))
print(arrmatriz[2][3]) # prefira pensar na notação como [linha, coluna]. Então, embora arrmatriz[2][3] funcione, a forma mais idiomática é arrmatriz[2,3].
print(arrmatriz[1][2:])
print(arrmatriz[:2,3:5])

# Exercício 3/5 — Indexação avançada

# Crie um array arr com os números de 1 a 20.

# Depois, usando uma única operação de indexação, mostre os elementos nos índices:

# 2, 7, 10 e 15

# na mesma ordem em que foram fornecidos.

import numpy as np

arrindexacao = np.arange(1,21)
print(arrindexacao[[2,7,10,15]])

# Exercício 4/5 — Máscara booleana

# Crie um array notas com 15 números inteiros aleatórios entre 0 e 100.

# Depois:

# Crie uma máscara que identifique as notas maiores ou iguais a 60.
# Use essa máscara para mostrar somente as notas aprovadas.
# Mostre quantas notas foram aprovadas.

import numpy as np

notas = np.random.randint(0,101,size=(15))

maiores = notas>=60
print(notas[maiores])
print(maiores.sum())

# Exercício 5/5 — Consolidando tudo

# Crie uma matriz dados com 5 linhas e 6 colunas, contendo números aleatórios entre 1 e 100.

# Depois faça tudo isso:

# Mostre o valor da linha 3, coluna 4.
# Mostre as linhas 1 e 2, somente nas colunas 2 até 4.
# Selecione as linhas 0, 2 e 4, nessa ordem.
# Crie uma máscara para identificar valores maiores que 50.
# Mostre somente os valores maiores que 50.
# Mostre quantos valores são maiores que 50.

import numpy as np

dados = np.random.randint(1,101,size=(5,6))
print(dados[3,4])
print(dados[1:3,2:5])
print(dados[[0,2,4]])
mascara_dados = dados > 50
print(dados[mascara_dados])
print(mascara_dados.sum())