# lambda

vezes_dois = lambda x : x * 2
# print(vezes_dois(2)) output: 4
# print(vezes_dois(3)) output: 6

lista = [405, 2093, 784, 2890, 105]
# print(max(list)) output: 2890
# print(min(list)) output: 105
# print(len(list)) output: 5
# print(type(list)) output: <class 'list'>

def tr ():
    tracos = print('-='*50)
    return tracos
# tr() output: -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# MOMENTO MAIS IMPORTANTE DE LAMBDA VEM AGORA

salarios = [2290, 3250, 2890, 4130, 1800]

salarios_atual = map(lambda x: x * 1.2,salarios) # output: <map object at 0x0000015F2A9CB8C0>
print(list(salarios_atual)) # output: [2748.0, 3900.0, 3468.0, 4956.0, 2160.0]

# Muito utilizados em Dataframes, método Apply