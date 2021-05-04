#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

tabuada = int(input("Digite um numero entre 1-10 para gerar a tabuada"))
for i in range(1,11):
    print("Tabuda: {} X {} = {} " .format(i, tabuada, i*tabuada))