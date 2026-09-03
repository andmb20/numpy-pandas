import numpy as np

a = 40
b = 70
# print(a>b)

cadastro = np.random.randint(15,51,size=(30,10))
cadastro_maior = cadastro > 18

# print(cadastro[cadastro_maior]) ou cadastro[cadastro>18]

print(len(cadastro[cadastro_maior]))
print(cadastro_maior.sum())

extraido = np.extract(cadastro_maior, cadastro)
print(len(extraido))