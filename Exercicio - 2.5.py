#Faça um programa para a leitura de duas notas parciais de 
# um aluno. O programa deve calcular a média alcançada por 
# aluno e apresentar:

# A - A mensagem "Aprovado", se a média alcançada for maior ou 
# igual a sete;
# B - A mensagem "Reprovado", se a média for menor do que sete;
# C - A mensagem "Aprovado com Distinção", se a média for igual 
# a dez.

print('Bem vindo!!')

n1 = int(input('Informe a primeira nota: '))
n2 = int(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

if media <= 9:
    print('Aluno aprovado!!')
elif media <= 4:
    print('Aluno reprovado!!')
elif media == 10:
    print('Aluno aprovado com Distinção!!')
else: 
    print('Erro!!')