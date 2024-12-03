#Crie um programa que contenha uma lista de números inteiros e, 
# utilizando um laço for, calcule e imprima a soma de todos os números 
# dessa lista.  Exemplo de lista: [3, 5, 7, 2, 8, 1] 
# Resultado esperado: 26 (porque 3 + 5 + 7 + 2 + 8 + 1 = 26)

lista = [3, 5, 7, 2, 8, 1, 50]
soma = 0

for num in lista:
    #print(num)
    soma = soma + num

print(soma)

