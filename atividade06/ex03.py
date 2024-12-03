login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

c = 1

while (login != "aluno" or senha != "123") and c <= 3:
    print("Acesso negado!")
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    c = c + 1

if login == "aluno" and senha == "123":
    print("Login realizado!")
else:
    print("Senha bloqueada")