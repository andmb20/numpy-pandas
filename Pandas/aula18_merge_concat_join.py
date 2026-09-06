# Como podemos unir DataFrames 

# Left join ou merge mantém todas as linhas da esquerda + correspondências da direita que coincidirem com a chave de ligação.

# Right join ou merge mantém todas as linhas da direita + correspondências da esquerda que coincidirem com a chave de ligação.

# Outer Join ou merge mantém todas as linhas de ambos os lados, mesmo sem correspondência; onde não houver dados, fica `NaN`/`NULL`.

# Inner Join ou merge mantém somente as linhas que possuem correspondência nos dois DataFrames pela chave.

import pandas as pd
import numpy as np

np.random.seed(100)

df1 = pd.DataFrame({
    'A': ['A0','A1','A2','A3'],
    'B': ['B0','B1','B2','B3'],
    'C': ['C0','C1','C2','C3'],
    'D': ['D0','D1','D2','D3']},
    index=[0,1,2,3])
df2 = pd.DataFrame({
    'A': ['A4','A5','A6','A7'],
    'B': ['B4','B5','B6','B7'],
    'C': ['C4','C5','C6','C7'],
    'D': ['D4','D5','D6','D7']},
    index=[4,5,6,7])
df3 = pd.DataFrame({
    'A': ['A8','A9','A10','A11'],
    'B': ['B8','B9','B10','B11'],
    'C': ['C8','C9','C10','C11'],
    'D': ['D8','D9','D10','D11']},
    index=[8,9,10,11])

dicionario = {'ID':[10,11,12,13,14],'Nome':['Ana','Bia','Carlos','Daniel','Eduardo'],'Cidade':['São Paulo','Rio de Janeiro','Belo Horizonte','Curitiba','Porto Alegre']}
dicionario2 = {'ID':[15,11,12,13,19],'Experiencia':['analista','junior','pleno','senior','especialista']}

df4 = pd.DataFrame(data=dicionario)
df5 = pd.DataFrame(data=dicionario2)

# Concatenando DataFrames
df_concat = pd.concat([df1, df2, df3])
# print(df_concat) output :
#                       A    B    C    D
#                 0    A0   B0   C0   D0
#                 1    A1   B1   C1   D1
#                 2    A2   B2   C2   D2
#                 3    A3   B3   C3   D3
#                 4    A4   B4   C4   D4
#                 5    A5   B5   C5   D5
#                 6    A6   B6   C6   D6
#                 7    A7   B7   C7   D7
#                 8    A8   B8   C8   D8
#                 9    A9   B9   C9   D9
#                 10  A10  B10  C10  D10
#                 11  A11  B11  C11  D11

df_concat2 = pd.concat([df1, df2], axis=1)
# print(df_concat2) output :
#                      A    B    C    D    A    B    C    D
#                 0   A0   B0   C0   D0  NaN  NaN  NaN  NaN
#                 1   A1   B1   C1   D1  NaN  NaN  NaN  NaN
#                 2   A2   B2   C2   D2  NaN  NaN  NaN  NaN
#                 3   A3   B3   C3   D3  NaN  NaN  NaN  NaN
#                 4  NaN  NaN  NaN  NaN   A4   B4   C4   D4
#                 5  NaN  NaN  NaN  NaN   A5   B5   C5   D5
#                 6  NaN  NaN  NaN  NaN   A6   B6   C6   D6
#                 7  NaN  NaN  NaN  NaN   A7   B7   C7   D7

# Merge DataFrames
merge_inner = pd.merge(df4,df5, how='inner')
# print(merge_inner) output :
#                ID    Nome          Cidade Experiencia
#             0  11     Bia  Rio de Janeiro      junior
#             1  12  Carlos  Belo Horizonte       pleno
#             2  13  Daniel        Curitiba      senior

merge_outer = pd.merge(df4,df5, how='outer')
print(merge_outer)
    # output :
    # ID     Nome          Cidade   Experiencia
    # 0  10      Ana       São Paulo           NaN
    # 1  11      Bia  Rio de Janeiro        junior
    # 2  12   Carlos  Belo Horizonte         pleno
    # 3  13   Daniel        Curitiba        senior
    # 4  14  Eduardo    Porto Alegre           NaN
    # 5  15      NaN             NaN      analista
    # 6  19      NaN             NaN  especialista

merge_esquerda = pd.merge(df4, df5, how='left')
print(merge_esquerda) 
    # output :
    #    ID     Nome          Cidade Experiencia
    # 0  10      Ana       São Paulo         NaN
    # 1  11      Bia  Rio de Janeiro      junior
    # 2  12   Carlos  Belo Horizonte       pleno
    # 3  13   Daniel        Curitiba      senior
    # 4  14  Eduardo    Porto Alegre         NaN

merge_direita = pd.merge(df4,df5,how='right')
print(merge_direita)
    # output :
    #    ID     Nome          Cidade Experiencia
    # 0  15      NaN             NaN   analista
    # 1  11      Bia  Rio de Janeiro     junior
    # 2  12   Carlos  Belo Horizonte      pleno
    # 3  13   Daniel        Curitiba     senior
    # 4  19      NaN             NaN especialista

dicionario3 = {'Nome':['Ana','Bia','Carlos','Daniel','Eduardo'],'Cidade':['São Paulo','Rio de Janeiro','Belo Horizonte','Curitiba','Porto Alegre']}
dicionario4 = {'Experiencia':['analista','junior','pleno','senior','especialista']}
df6 = pd.DataFrame(data=dicionario3)
df7 = pd.DataFrame(data=dicionario4)

# Join DataFrames
# Join é uma forma de combinar DataFrames com base no índice. Por padrão, o join é feito à esquerda (left join), mas você pode especificar outros tipos de join usando o parâmetro `how`.
join_esquerda = df6.join(df7)
print(join_esquerda)
# output : 
#       Nome          Cidade   Experiencia
# 0      Ana       São Paulo      analista
# 1      Bia  Rio de Janeiro        junior
# 2   Carlos  Belo Horizonte         pleno
# 3   Daniel        Curitiba        senior
# 4  Eduardo    Porto Alegre  especialista


