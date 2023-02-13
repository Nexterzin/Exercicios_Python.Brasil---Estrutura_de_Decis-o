#Faça um Programa que verifique se uma letra digitada 
# é "F" ou "M". Conforme a letra escrever: F - Feminino, 
# M - Masculino, Sexo Inválido.

print('Bem vindo!!')

genero = input('Informe o uma das letra: M / F: ')

if genero == 'M':
    print('M - Masculino!!')
elif genero == 'F':
    print('F - Feminino!!')
else:
    print('Sexo invalido!!')