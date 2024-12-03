#Crie um programa que leia o um nome escrito pelo usuário e pergunte qual
#a letra ele quer verificar. O programa deve dizer se a letra existe e 
# qual a quantidade. 

palavra = 'PyThON'
palavra_maiucula = palavra.upper() 
palavra_minuscula = palavra.lower()

print(palavra)
print(palavra_maiucula)
print(palavra_minuscula)

nome = input("Digite um nome: ")
letra_buscada = input("Qual letra quer verificar? ")
contador = 0

for letra in nome:
    if letra_buscada.upper() == letra.upper():
        #print('Letra encontrada!')
        contador = contador + 1

if contador > 0:
    print(f"A letra {letra_buscada} foi encontrada {contador} vezes!")
else:
    print(f"A letra {letra_buscada} não foi encontrada!")
