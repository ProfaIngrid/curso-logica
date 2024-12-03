'''
Desenvolver um programa que permita calcular o valor total das compras 
feitas por um cliente, aplicando um desconto de 5% para pagamentos 
realizados via PIX ou débito, e exibindo o valor das parcelas para 
pagamentos em crédito. O programa deverá fazer uso de laços de repetição 
e funções para estruturar as operações.

Descrição:
-O programa deverá começar solicitando ao usuário o número de produtos 
    que ele comprou.
-Para cada produto, o programa deve receber o nome e o preço.
-Ao final, o programa calculará o valor total da compra.
-O cliente poderá escolher a forma de pagamento entre PIX, débito ou 
    crédito.
-Se a forma de pagamento for PIX ou débito, o programa deve aplicar um 
    desconto de 5% sobre o valor total.
-Se a forma de pagamento for crédito, o programa deverá perguntar em 
    quantas parcelas o cliente deseja dividir o valor. O valor de cada 
    parcela será calculado, sem juros adicionais.
-O programa deve exibir o valor total, o valor do desconto (se aplicável)
    ou o valor das parcelas (se for em crédito), conforme o tipo de
    pagamento.
'''
def total_compras(precos):
    total = 0
    for preco in precos:
       total = preco + total
    return total

def desconto(total, pagamento):
    if pagamento == 1 or pagamento == 2: #pix ou débito
        desconto = total * 0.05
        total_desconto = total - desconto
        return total_desconto
    else:
        return total #no caso do crédito, não tem desconto

def parcelamento(total, parcelas):
    valor_parcela = total / parcelas
    return valor_parcela

#recebo a quantidade de produtos
n = int(input("Quantos produtos vai comprar? ")) 

#listas para armazenar o nome e valor de cada produto
produtos = []
precos = []

#solicitando e armazenando cada produto, um por vez
for i in range(n):
    nome = input("Nome do produto: ")
    preco = float(input("Valor do produto: "))
    produtos.append(nome)
    precos.append(preco)

total = total_compras(precos)
print("O total da compra foi: ", total)

print("Escolha a forma de pagamento:")
print("1 - Pix")
print("2 - Débito")
print("3 - Crédito")
pagamento = int(input("Digite sua forma de pagamento: "))

if pagamento == 1 or pagamento == 2:
    valorComDesconto = desconto(total, pagamento)
    print(f"Você recebeu 5% de desconto")
    print(f"Seu desconto foi de R$ {(total-valorComDesconto):.2f}")
    print(f"O valor final é R$ {valorComDesconto:.2f}")
elif pagamento == 3:
    parcelas = int(input("Em quantas parcelas deseja dividir? "))
    valorParcela = parcelamento(total, parcelas)
    print(f"O valor de cada parcela será de R$ {valorParcela:.2f} em {parcelas} parcelas")
else:
    print("Opção inválida!")

