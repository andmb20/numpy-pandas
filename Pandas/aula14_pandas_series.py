# PANDAS é baseado em Series, representado em forma de coluna
import numpy as np
import pandas as pd

s = pd.Series([1,2,3,'olá',np.nan,6,8])
# print(s) output :
                    # 0      1
                    # 1      2
                    # 2      3
                    # 3    olá
                    # 4    NaN
                    # 5      6
                    # 6      8
                    # dtype: object

# Series a partir de uma lista

lista = [10,20,30,40,50]
# print(pd.Series(lista)) output :
                    # 0    10
                    # 1    20
                    # 2    30
                    # 3    40
                    # 4    50
                    # dtype: int64

# Series a partir de um dicionário

dicionario = {
    'tel1': '9999',
    'tel2': '8888',
    'tel3': '7777'
}
# print(pd.Series(dicionario)) output :
                    # tel1    9999
                    # tel2    8888
                    # tel3    7777
                    # dtype: str

# Series a partir de um array

arr = np.array([10,30,20,50,40]) # output : [10 30 20 50 40]

arrSeries = pd.Series(arr)
# print(arrSeries) output :
                    # 0    10
                    # 1    30
                    # 2    20
                    # 3    50
                    # 4    40
                    # dtype: int64

# Alterando indice do Series

indSeries = pd.Series([1,2,3,4], index=['Brasil', 'EUA', 'Argentina', 'China'])
# print(indSeries) output :
                    # Brasil       1
                    # EUA          2
                    # Argentina    3
                    # China        4
                    # dtype: int64

listSeries = [2,4,6,8]
labelsSeries = ['Argentina', 'Japão', 'Brasil', 'Espanha']

# print(pd.Series(data=listSeries,index=labelsSeries)) output :
                    # Argentina  2
                    # Japão      4
                    # Brasil     6
                    # Espanha    8
                    # dtype: int64

print(indSeries+pd.Series(data=listSeries,index=labelsSeries)) # output :
                    # Argentina    5.0
                    # Brasil       7.0
                    # China        NaN
                    # EUA          NaN
                    # Espanha      NaN
                    # Japão        NaN
                    # dtype: float64