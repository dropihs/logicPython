#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

#reaproveitei codigo do exercicio 14 

nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota do {} ".format(nome))) #A funcao de input só aceita o .format para printar variavel (sem virgula)
nota2 = float(input("Digite a segunda nota do {} ".format(nome)))
media = (nota1 + nota2)/2 

if media == 10: 
    print("Aprovado com distinção")
    conceito = 'A' 
elif media >= 9 and media <= 10:
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
