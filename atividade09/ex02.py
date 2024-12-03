#Crie um programa que contenha uma lista de números inteiros de 1 a 20
#  (usando o range). Utilize um laço for para criar uma nova lista
#  contendo apenas os números pares da lista original e imprima essa nova
#  lista.

lista = list(range(1, 21))
lista_pares = []

for numero in lista:
    if numero%2 == 0:
        lista_pares.append(numero)

print(lista_pares)

