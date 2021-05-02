# 24.	Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# .	"Telefonou para a vítima?"
# a.	"Esteve no local do crime?"
# b.	"Mora perto da vítima?"
# c.	"Devia para a vítima?"
# d.	"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

##Se a pessoa responder positivamente a 2 questões ela deve ser
#classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como
#“Assassino”. Caso contrário, ele será classificado como “Inocente”

print("(1)Sim (2)Não")
q1 = int(input("Telefonou pra vitima?"))
 
q2 = int(input("Esteve no local do crime?"))

q3 = int(input("Mora perto da vitima?"))

q4 = int(input("Devia para a vitima?"))

q5 = int(input("Já trabalhou com a vitima?"))

somador = 0

if q1 == 1:
   somador = somador + 1 
elif q1 == 2: 
    somador = somador - 1 

if q2 == 1:
   somador = somador + 1
elif q2 == 2: 
    somador = somador - 1 

if q3 == 1:
   somador = somador + 1
elif q3 == 2: 
    somador = somador - 1

if q4 == 1:
   somador = somador + 1
elif q4 == 2: 
    somador = somador - 1

if q5 == 1:
   somador = somador + 1
elif q5 == 2: 
    somador = somador - 1

print("somador: ",somador)

if somador == 5:
    print("Assasino")
elif 3 <= somador <= 4:
    print("Cumplice")
elif somador == 2: 
    print("Suspeito")
elif somador == -5:
    print ("Inocente")
else: #Pra quem respondeu entre 1 - 4 não
    print("Ficar de olho")