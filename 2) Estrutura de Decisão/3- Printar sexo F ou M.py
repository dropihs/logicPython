# 3.	Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
# letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
dig = input("Digite o sexo (F) ou (M)")
if dig == "F" or dig == "f":
    print("Sexo escolhido Feminino")
elif dig == "M" or dig == "m":
    print("Sexo escolhido Masculino")
else:
    print("Sexo não definido")
