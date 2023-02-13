#Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# mprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
# "Valor Inválido!", conforme o caso.

print('Bem vindo!!')

horario = input("Informe o horario que voce estuda\n M-Matutino\n V-Vespetino\n N-Noturno\n ")


if horario == 'M':
    print('Bom dia!!')
elif horario == 'V':
    print('Boa tarde!!')
elif horario == 'N':
    print('Boa noite!!')
else:
    print('Valor invalido!!!')