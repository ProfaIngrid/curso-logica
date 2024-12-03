#Crie um programa que contenha uma lista de números inteiros. Utilize um 
# laço for para percorrer a lista e encontrar o maior número. O programa 
# deve imprimir o maior número da lista.  Exemplo de lista: 
# [3, 5, 7, 2, 8, 1]

lista_numeros = [3, 5, 7, 2, 8, 1] #[-8, -9, -1, -5]
maior = lista_numeros[0]

for numero in lista_numeros: 
    # print(numero)
    if maior < numero:
        print("Troca foi feita entre ", maior, 'e', numero)
        maior = numero

print("O maior valor é", maior)
