anoAtual = int(input("Digite o ano atual: "))
idade = int(input("Digite sua idade: "))
fezAniversario = input("Fez aniversário esse ano? ")

if fezAniversario == 'sim':
    ano = anoAtual - idade
else: 
    ano = anoAtual - 1 - idade

print("Você nasceu em", ano)