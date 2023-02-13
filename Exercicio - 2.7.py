#Faça um Programa que leia três números e mostre 
# o maior e o menor deles.

print('Bem vindo!!')

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segunda numero: '))
n3 = int(input('Informe o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)

if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
else:
    print(n3)
