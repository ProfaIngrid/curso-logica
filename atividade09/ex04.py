# Crie um programa que contenha uma lista de números inteiros. Utilize
# um laço for para criar uma nova lista com os elementos da lista 
# original, mas na ordem inversa, e imprima essa nova lista.

lista = [5, 8, 1, 3, 7, 10, 2]
lista_reversa = []


for num in lista: 
   lista_reversa.insert(0, num)
   print(lista_reversa)



