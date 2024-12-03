nomes = ["Ana", "João", "Paula", "Matheus"]
idades = [18, 26, 15, 25]

#exibindo a lista completa
print(nomes)
print(idades)

print(f'\n{'#'*80}\n') #quebra de linha e separação com #

print("Acessando o primeiro nome da lista nomes: ", nomes[0]) #nomes[0]
print("Acessando a segunda idade da lista idades: ", idades[1]) #idades[1]

print('\n', '#'*80, '\n')

#o tamanho de uma lista é retornado pela função len()
print("Tamanho da lista nomes: ", len(nomes)) #len(nomes)
print("Tamanho da lista idades: ", len(idades)) #len(idades)


print(f'\n{'#'*80}\n') #quebra de linha e separação com #

print("Idades sem modificação:", idades)
idades[2] = 16 #alterando o valor da posição 2 para 16
print("Idades após a modificação:", idades)

print(f'\n{'#'*80}\n') #quebra de linha e separação com #

print("Nomes sem modificação:", nomes)
#adicionando um novo nome na lista nomes na ultima posição
nomes.append("Carlos") 
print("Nomes após a modificação:", nomes)

print(f'\n{'#'*80}\n') #quebra de linha e separação com #

print("idades sem modificação:", idades)
#insere um novo item na lista baseado na posição 
#insert(posicao, valor)
idades.insert(1, 50) 
print("idades após a modificação:", idades)

print(f'\n{'#'*80}\n') #quebra de linha e separação com #

print("Nomes sem modificação:", nomes)
#removendo um item por valor da lista
nomes.remove("Ana") 
print("Nomes após a modificação:", nomes)

print(f'\n{'#'*80}\n') #quebra de linha e separação com #

print("idades sem modificação:", idades)
#removendo um item por posição da lista
idades.pop(2)
print("idades após a modificação:", idades)

print(f'\n{'#'*80}\n') #quebra de linha e separação com #

print("Nomes sem ordenação:", nomes)
#para ordenar uma lista usamos o sort() (alfabetica ou númerica)
nomes.sort() #sort(reverse=True) 
print("Nomes após a ordenação:", nomes)

print(f'\n{'#'*80}\n') #quebra de linha e separação com #

print("idades sem reversão:", idades)
#para reverter uma lista usamos o reverse()
idades.reverse()
print("idades após a reversão:", idades)

print(f'\n{'#'*80}\n') #quebra de linha e separação com #

print("Lista nomes: ", nomes)
#index() retorna a posição em que o valor esta localizado
paula = nomes.index("João") 
print("João esta na posição:", paula)

