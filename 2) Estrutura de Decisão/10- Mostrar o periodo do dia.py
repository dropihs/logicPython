# 10.	Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
perido = input("M-matutino ou V-Vespertino ou N- Noturno.")

if perido == 'm' or perido == 'M':
    print("Bom dia!")

elif perido == 'v' or perido == 'V':
    print("Boa tarde!")

elif perido == 'n' or perido == 'N':
    print("Boa noite!")
