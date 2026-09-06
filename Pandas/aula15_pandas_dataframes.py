import pandas as pd
import numpy as np

# Criação de Dataframes a partir de um array

arr = np.random.randint(10,55,size=[4,4])
# print(arr)

dataFrame = pd.DataFrame(arr)# ou pd.DataFrame(data=arr) 
# print(dataFrame)

dataFrame2 = pd.DataFrame(data=arr, index=['A','B','C','D'], columns=['W','X','Y','Z'])
# print(dataFrame)

# O pandas DataFrame entende uma lista como os dados de uma coluna. 1 dimensão
lista = [10,20,30,40,50]
dataFrame3 = pd.DataFrame(data=lista)
# print(dataFrame3) output :
                    #     0
                    # 0  10
                    # 1  20
                    # 2  30
                    # 3  40
                    # 4  50

# Uma lista de listas representa linhas e colunas do DataFrame. 2 dimensão
lista2 = [[10,20,30,40,50],[60,70,80,90,100]]
dataframe4 = pd.DataFrame(data=lista2)
# print(dataframe4) output :
#                         0   1   2   3    4
#                     0  10  20  30  40   50
#                     1  60  70  80  90  100

dataframe5 = pd.DataFrame(data=lista2,index=('A','B'),columns=('V','W','X','Y','Z'))
# print(dataframe5) output :
#                         V   W   X   Y    Z
#                     A  10  20  30  40   50
#                     B  60  70  80  90  100

# Criação de DataFrames através de um dicionário
dados = {
    'Produtos':['PS5','Notebook','Mouse','Teclado','Fone'],
    'Preços':[4200,4500,30,60,80]
    }
dataFrame6 = pd.DataFrame(dados)
# print(dataFrame6) output :
#                        Produtos  Preços
#                     0       PS5    4200
#                     1  Notebook    4500
#                     2     Mouse      30
#                     3   Teclado      60
#                     4      Fone      80

dataFrame6['Custo'] = [3700,3900,12,26,45]
dataFrame7 = pd.DataFrame(dataFrame6)
# print(dataFrame7) output :
#                        Produtos  Preços  Custo
#                     0       PS5    4200   3700
#                     1  Notebook    4500   3900
#                     2     Mouse      30     12
#                     3   Teclado      60     26
#                     4      Fone      80     45

dataFrame7['Lucro'] = dataFrame7['Preços'] - dataFrame7['Custo']
dataFrame8 = pd.DataFrame(dataFrame7)
# print(dataFrame8) output :
#                        Produtos  Preços  Custo  Lucro
#                     0       PS5    4200   3700    500
#                     1  Notebook    4500   3900    600
#                     2     Mouse      30     12     18
#                     3   Teclado      60     26     34
#                     4      Fone      80     45     35
