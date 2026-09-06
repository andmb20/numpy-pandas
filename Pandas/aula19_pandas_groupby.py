import pandas as pd
import numpy as np

data = {'Sede':['SP','SP','SP','RJ','RJ','RJ'],
        'Vendedor':['João','Maria','José','Ana','Bia','Carlos'],
        'Vendas':[1000,1500,2000,3000,2500,4000]}
df = pd.DataFrame(data=data)

# print(df)
# output :
#   Sede Vendedor  Vendas
# 0   SP     João    1000
# 1   SP    Maria    1500
# 2   SP     José    2000
# 3   RJ      Ana    3000
# 4   RJ      Bia    2500
# 5   RJ   Carlos    4000

by_sede = df.groupby('Sede')
# print(by_sede.max())
# output :
#      Vendedor  Vendas
# Sede                 
# RJ     Carlos    4000
# SP      Maria    2000

# print(by_sede.describe())
# output :
#      Vendas                                                                 
#       count         mean         std     min     25%     50%     75%     max
# Sede                                                                        
# RJ      3.0  3166.666667  763.762616  2500.0  2750.0  3000.0  3500.0  4000.0
# SP      3.0  1500.000000  500.000000  1000.0  1250.0  1500.0  1750.0  2000.0

# print(by_sede.describe().transpose())
# output :
# Sede                   RJ      SP
# Vendas count     3.000000     3.0
#        mean   3166.666667  1500.0
#        std     763.762616   500.0
#        min    2500.000000  1000.0
#        25%    2750.000000  1250.0
#        50%    3000.000000  1500.0
#        75%    3500.000000  1750.0
#        max    4000.000000  2000.0

# print(by_sede.describe().transpose()['RJ'])
# output :
# Vendas  count       3.000000
#         mean     3166.666667
#         std       763.762616
#         min      2500.000000
#         25%      2750.000000
#         50%      3000.000000
#         75%      3500.000000
#         max      4000.000000
# Name: RJ, dtype: float64

arrays = [['São Paulo','São Paulo','Rio de Janeiro','Rio de Janeiro','Minas Gerais','Minas Gerais'],
          ['Garrafas','Copos','Garrafas','Copos','Garrafas','Copos']]
index = pd.MultiIndex.from_arrays(arrays,names=('Estado','Produto'))
df2 = pd.DataFrame(data={'Vendas':[1000,1500,2000,3000,2500,4000]},index=index)
# print(df2)
# output :
#                          Vendas
# Estado         Produto         
# São Paulo      Garrafas    1000
#                Copos       1500
# Rio de Janeiro Garrafas    2000
#                Copos       3000
# Minas Gerais   Garrafas    2500
#                Copos       4000

mult_byestado = df2.groupby('Estado',level=0)
print(mult_byestado.mean())
# output :
#                 Vendas
# Estado                
# Minas Gerais    3250.0
# Rio de Janeiro  2500.0
# São Paulo       1250.0

mult_byproduto = df2.groupby('Produto',level=1)
print(mult_byproduto.mean())
# output :
#                Vendas
# Produto              
# Copos     2833.333333
# Garrafas  1833.333333
