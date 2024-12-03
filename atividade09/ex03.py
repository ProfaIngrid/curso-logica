#Crie um programa que contenha uma lista com alguns números inteiros,
#  positivos e negativos. Utilize um laço for para contar quantos números
#  negativos existem na lista e imprima essa quantidade.

lista = [-5, -9, -8, 0, 5, 4, 10, 20, -12]
cont_negativos = 0

for num in lista:
    if num < 0:
        cont_negativos = cont_negativos + 1

print(f"Existem {cont_negativos} numeros negativos dentro da lista {lista}")
