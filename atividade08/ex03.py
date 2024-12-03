#Crie um programa que contenha uma lista com os números de 1 a 5. Utilize
#um laço for para criar uma nova lista com o quadrado de cada número 
# dessa lista original. O programa deve imprimir a nova lista.  Exemplo 
# de lista original: [1, 2, 3, 4, 5] Resultado esperado: [1, 4, 9, 16, 25]

lista = list(range(1, 6)) #crio uma lista de 1 a 5
nova_lista = []

for i in lista:
    #print(i**2)
    nova_lista.append(i**2)

    print(nova_lista)
