def exibeNome(nome):
    return print(f"Bem-vindo(a), {nome}!")

def leDado(tipo, texto):
    if tipo == 'str':
        dado = input(texto)
    elif tipo == 'int':
        dado = int(input(texto))
    elif tipo == 'float':
        dado = float(input(texto))
    return dado

#chama a função leNome para guardar o nome de um usuário e guarda na 
#variavel n 
n = leDado('str', "Digite o seu nome: ") 
idade = leDado('int', "Digite a sua idade: ")

#chama a função a função exibeNome usando o nome que foi armazenado na 
#variavel n
exibeNome(n)



