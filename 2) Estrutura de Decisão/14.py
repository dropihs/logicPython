#14.  Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece
#     à tabela abaixo:
#o	  Média de Aproveitamento  Conceito
#o	  Entre 9.0 e 10.0        A
#o	  Entre 7.5 e 9.0         B
#o	  Entre 6.0 e 7.5         C
#o	  Entre 4.0 e 6.0         D
#o	  Entre 4.0 e zero        E
#     O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota do {} ".format(nome))) #A funcao de input só aceita o .format para printar variavel (sem virgula)
nota2 = float(input("Digite a segunda nota do {} ".format(nome)))
media = (nota1 + nota2)/2 

if media >= 9 and media <= 10:
    conceito = 'A' 
elif media >= 7.5  and media < 9:
    conceito = 'B'
elif media >= 6  and media < 7.5:
    conceito = 'C'
elif media >= 4  and media < 6:
    conceito = 'D'
elif media >= 0  and media <= 4:
    conceito = 'E'

print("Conceito de {}: {}" .format(nome, conceito))

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print("Aprovado")
elif conceito == 'D' or 'E': 
    print("Reprovado")
