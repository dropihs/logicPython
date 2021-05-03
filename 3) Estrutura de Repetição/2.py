#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

login = input("Cadastre o login: ")
senha = input("Cadastre a senha: ")

acessoLogin = input("Digite o login: ")
acessoSenha = input("Digite a senha: ")
while acessoLogin != login and acessoSenha != senha:
    print("Login ou senha incorreto,tente novamente")
    acessoLogin = input("Digite o login: ")
    acessoSenha = input("Digite a senha: ")

print("Acesso permitido")
