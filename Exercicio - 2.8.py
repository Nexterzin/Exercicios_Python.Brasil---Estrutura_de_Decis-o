#Faça um programa que pergunte o preço de três produtos 
# e informe qual produto você deve comprar, sabendo que a 
# decisão é sempre pelo mais barato.

print('Bem vindo!!')

print('Qual fruta quer escolher?\n 1 - banana - R$5,00\n 2 - laranja R$9,00\n 3 - pera R$2,00\n')

n1 = 5
n2 = 9
n3 = 2


if n1 < n2 and n1 < n3:
    print('Banana')
elif n2 < n1 and n2 < n3:
    print('Laranja')
else:
    print('Pera')
