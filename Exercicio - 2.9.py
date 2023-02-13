#Faça um Programa que leia três números e mostre-os 
# em ordem decrescente.

print('Bem vindo!!')

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))
n3 = int(input('Informe o terceiro numero: '))

if n1 > n2 and n1 > n3 and n2 > n3:
    print(n1,n2,n3)
if n2 > n1 and n2 > n3 and n1 > n3:
    print(n2,n1,n3)
if n3 > n2 and n3 > n1 and n2 > n1:
    print(n3,n2,n1)
    