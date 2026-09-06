# MultiIndex ou seja, varios indices ( cada indice com um nível )

import pandas as pd
import numpy as np

lista = [['Brasil','Brasil','Brasil','Argentina','Argentina','Argentina'],[2017,2018,2019,2017,2018,2019]]

tuplas = zip(*lista)
# print(tuplas) output : <zip object at 0x000002D0456FFA40>
tuplas = list(tuplas)
# print(tuplas) output : [('Brasil', 2017), ('Brasil', 2018), ('Brasil', 2019), ('Argentina', 2017), ('Argentina', 2018), ('Argentina', 2019)]

multi = pd.MultiIndex.from_tuples(tuplas)
# print(multi) output :
#                     MultiIndex([(   'Brasil', 2017),
#                                 (   'Brasil', 2018),
#                                 (   'Brasil', 2019),
#                                 ('Argentina', 2017),
#                                 ('Argentina', 2018),
#                                 ('Argentina', 2019)],
#                             )

df1 = pd.DataFrame(data = np.random.randn(6,2),index=multi,columns=['EXP TRIGO','EXP SOJA'])
# print(df1) output :
#                                 EXP TRIGO  EXP SOJA
#                 Brasil    2017   0.989179  1.332474
#                           2018  -1.713985 -1.435611
#                           2019  -1.719399 -0.217985
#                 Argentina 2017   1.081018 -1.735067
#                           2018   1.694233 -1.205333
#                           2019  -0.120760  0.451366

df1.index.names = ['País','Ano']
# print(df1) output :
#                                 EXP TRIGO  EXP SOJA
#                 País      Ano                      
#                 Brasil    2017  -0.366646 -0.413210
#                           2018   0.906503 -0.604174
#                           2019   0.543801  1.281410
#                 Argentina 2017  -1.131495 -0.861453
#                           2018   0.226503 -1.310743
#                           2019  -0.298750  0.335893

# print(df1['EXP SOJA'])
# print(df1.loc['Brasil'])
# print(df1.xs(2017, level=1)) output :
#                        EXP TRIGO  EXP SOJA
#             País                          
#             Brasil     -2.007653  1.545306
#             Argentina   1.015904  0.913038
# print(df1[:3])
# print(df1[['EXP SOJA','EXP TRIGO']]) Tras as colunas na ordem que eu solicitei

df2 = df1.unstack()
# print(df2) output :
#                         EXP TRIGO                      EXP SOJA                    
#                 Ano            2017      2018      2019      2017      2018      2019
#                 País                                                                 
#                 Argentina  0.466474 -0.081975 -1.552572 -0.204235  0.530403 -1.094965
#                 Brasil    -1.384637  0.151340  1.638813  0.010157  0.578759 -1.677413

print(df2.xs(2017,axis=1,level=1))