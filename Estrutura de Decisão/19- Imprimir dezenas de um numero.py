#19.Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input("Digite um numero 1-1000:   "))

if num < 1000 and num > 0:
    if 100 <= num <= 999:
        u = num % 10
        d = num % 100
        c = num % 1000
        print("Centena: ", str(c)[0], "\nDezena: ", str(d)[0], "\nUnidade: ", str(u)[0]) #dezena nao printa 0 WHYYYYYYYYYYYY
    elif 10 < num <= 99: 
        u = num % 10
        d = num % 100
        print("\nDezena: ", str(d)[0], "\nUnidade: ", str(u)[0])
    elif 1 <= num <= 9: 
        u = num % 10
        print("Unidade: {}\n".format(u))
else: 
    print("Digito errado")

