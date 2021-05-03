#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome(maior que 3 caracteres)")
while len(nome) < 3:
    print("Nome não aceito digite novamente")
    nome = input("Digite seu nome(maior que 3 caracteres)")

print("Nome aceito")

idade = int(input("Digite sua idade(entre 0 e 150)"))
while idade >= 150 and idade <= 0:
    print("idade não aceita")
    idade = int(input("Digite sua idade(entre 0 e 150)"))

print("Idade aceita")

salario = float(input("Digite seu salario(salario maior que)"))
while salario <= 0:
    print("Salario não aceito")
    salario = float(input("Digite seu salario(salario maior que)"))

print("Salario aceito")

sexo = str(input("Digite o sexo (m ou f)"))
while sexo != 'f' and sexo != 'm':
    print("Sexo incorreto")
    sexo = str(input("Digite o sexo (m ou f)"))

print("Sexo aceito")

estadoCivil = input("Digite o estado civil ('s', 'c', 'v', 'd';)")
while estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd':
    print("estado civil incorreto")
    estadoCivil = input("Digite o estado civil ('s', 'c', 'v', 'd';)")


print("=================================================")
print(nome, idade, salario, sexo, estadoCivil)