"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
 O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder 
 positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
 Caso contrário, ele será classificado como "Inocente".
 """
print("Responda sim ou nao")
pergunta = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?",  "Devia para a vítima?", "Já trabalhou com a vítima?" ]
cont = 0 

for i in range(5):
    print(pergunta[i])
    resposta = input("Resposta: ")
    if resposta == "sim": 
        cont += 1 
    elif resposta == "nao":
        cont += 0 
print(cont)
if cont >= 5: 
    print("Assasino")
elif cont >= 3 and cont <= 4: 
    print("Cumplice")
elif cont == 2:
    print("Suspeito")
else: 
    print("Inocente")

