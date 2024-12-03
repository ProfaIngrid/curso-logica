produtos = ["Arroz", "Feijão", "Óleo", "Açúcar", "Macarrão"]
quantidades = [10, 25, 5, 20, 15]

#1 - Exiba as listas completas de produtos e quantidades.
print("Produtos: ", produtos)
print("Quantidade: ", quantidades)

#2 - Acesse e imprima:
##2.1 - O nome do primeiro produto da lista produtos.
print("O 1º produto é", produtos[0])

##2.2 - A segunda quantidade da lista quantidades.
print("A 2ª quantidade é: ", quantidades[1])

#3 - Verifique e imprima o tamanho das listas produtos e quantidades.
print("Tamanho da lista produtos:", len(produtos))
print("Tamanho da lista quantidade: ", len(quantidades))

#4 - Modifique a quantidade do terceiro produto para um novo valor 
# (exemplo: 30) e imprima a lista de quantidades após a modificação.
quantidades[2] = 30
print("Quantidades apos modificação:", quantidades)

#5 - Adicione um novo produto (exemplo: "Sal", com a quantidade 40) ao 
# final da lista produtos e imprima a lista de produtos atualizada.
print("Lista atual: ", produtos)
produtos.append("Sal")
quantidades.append(40)
print("Lista modificada:", produtos)

#6 - Insira um novo produto (exemplo: "Café", com a quantidade 10) na
# segunda posição (índice 1) da lista produtos e quantidades, e imprima 
# as listas após a inserção.
print("Listas: ", produtos, quantidades)
produtos.insert(1, "Café")
quantidades.insert(1, 10)
print("Listas Alterada: ", produtos, quantidades)

#7 - Remova um produto da lista produtos pelo nome (exemplo: "Feijão") e 
# imprima a lista de produtos atualizada.
print("Lista produtos: ", produtos)
produtos.remove("Feijão")
print("Lista produtos: ", produtos)

#8 - Remova um produto da lista quantidades baseado na posição 
# (por exemplo, remova o produto na posição 2) e imprima a lista de 
# quantidades após a remoção.
print("Lista quantidade: ", quantidades)
quantidades.pop(2)
print("Lista quantidade: ", quantidades)

#9 - Ordene a lista de produtos em ordem alfabética e imprima a lista 
# ordenada.
produtos.sort()
print("Produtos ordenados: ", produtos)

#10 - Inverta a lista de quantidades e imprima a lista de quantidades 
# após a reversão.
quantidades.reverse()
print("Lista quantidades reversa:", quantidades)

#11 - Localize a posição de um produto específico na lista produtos e 
# imprima o índice em que o produto se encontra.
# acucar = produtos.index("Açúcar")
# print(acucar)
print(produtos.index("Açúcar"))