import pandas as pd
import numpy as np
np.random.seed(100)

indices = ['Janeiro','Março','Maio','Julho','Agosto','Outubro','Dezembro']
colunas = np.arange(1,32)

dados = np.random.randint(632,2048,size=(7,31))
# print(dados)

df = pd.DataFrame(data=dados,index=indices,columns=colunas)
# print(df)
# df[coluna]
# df[[coluna1, coluna2, coluna3...]]
# df[coluna][linha]
# df[linha:linha]
# df.loc[indice linha, indice coluna] = df.loc['Julho',30]
# df.iloc[indice numerico da linha, indice numerico da coluna] = df.loc[3,30]
# df.loc[linha1,linha2...],[coluna1,coluna2...]

# Quanto vendeu no dia 10 de todos os meses ?

# print(df[10]) output :
#                     Janeiro     1972
#                     Março       1438
#                     Maio        1836
#                     Julho        918
#                     Agosto      2045
#                     Outubro     1285
#                     Dezembro     745
#                     Name: 10, dtype: int32

# Quanto vendeu no dia 10,20,30 de todos os meses ?

# print(df[[10,20,30]]) output :
#                                 10    20    30
#                     Janeiro   1972  1660   634
#                     Março     1438   649  1841
#                     Maio      1836  1732  1078
#                     Julho      918  1435  1344
#                     Agosto    2045  1945  1871
#                     Outubro   1285  1636  1954
#                     Dezembro   745  1511  1229

# Quanto vendu no dia 15 de Março ?
# print(df[15]['Março']) output : 1562

# Quanto vendeu os meses de Janeiro, Março e Maio ?
# print(df[0:3]) output :
#            1     2     3     4     5     6     7     8     9     10    11    12   13    14    15    16    17    18    19    20    21    22    23    24    25    26    27    28    29    30    31
# Janeiro  1424   711   982   685  1434  1641  1384   912  1884  1972  1544  1749  718  1018  1047  1529  1797  1389  1244  1660  1235  1467   767   681   949  1414  1599  1395  1992   634  1521
# Março    1249  1110   695  1837   915  1894  2025  1576  1959  1438   804   906  824  1584  1562  1069   905  1250  1686   649  1709   700  1120  2003  1107  1325  1478  1656   645  1841   994
# Maio      763  1214  1868  1026  1871  1127  1275  1505  1832  1836   668  1471  670  1870  1750  1370  1826  1484   727  1732   946   734  1570  1038  1912  1394   858  1547   828  1078  1450

# Quanto vendeu nos meses de Julho, Agosto e Outubro nos dias 25 a 31 ?

# print(df.loc[['Julho','Agosto','Outubro'],[25,26,27,28,29,30,31]]) output :
#                                25    26    27    28    29    30    31
#                     Julho    1879  1420   770  1408  1105  1344  1645
#                     Agosto   1354  1146  1207  1513  1786  1871   777
#                     Outubro  1323  1386  1138  1325  1337  1954   804

# print(df.iloc[[3,4,5],[24,25,26,27,28,29,30]]) output :
                    #            25    26    27    28    29    30    31
                    # Julho    1879  1420   770  1408  1105  1344  1645
                    # Agosto   1354  1146  1207  1513  1786  1871   777
                    # Outubro  1323  1386  1138  1325  1337  1954   804


# df.iloc[indice numerico da linha, indice numerico da coluna] = df.loc[3,30]
# df.loc[linha1,linha2...],[coluna1,coluna2...]


# Seleção Condicional de Dataframes

# print(df)

df.rename({
    'Dezembro': 'DEZEMBRO'
}, inplace=True)

# print(df)

# print(df[df > 1000]) output nan onde é menor que 1000
# print(df[df > 1000].fillna('-')) output nan = a -

# print(df[df > 1000][0:3].fillna('-'))
# print(df[df > 1000][:][[1,2,3,4,5]].fillna('-'))

# print(df[(df[10] > 1000)])
# print(df[(df[10] > 1000) & (df[15] > 1500)]) Retorna todas linhas que atendem a essas condições 
# print(df[(df[10] > 1500) | (df[15] > 1600)]) Retorna todas linhas que atendem a essas condições 