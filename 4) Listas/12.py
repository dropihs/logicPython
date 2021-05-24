# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos 
# alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
import random 

altura = []
idade = []

for i in range(30):
    altura.append(random.uniform(1.5,2.0))
    idade.append(random.randint(10,19))
media = sum(altura)/len(altura)
print(altura)
print(idade)
for i in range(30):
    if idade[i] > 13 and altura[i] < media: 
        print("Altura: ",altura[i])
        print("Idade: ",idade[i])