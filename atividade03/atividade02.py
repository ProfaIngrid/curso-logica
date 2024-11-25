saldoConta = float(input("Qual o saldo da conta? "))
valorProduto = float(input("Qual o valor do produto? "))

if saldoConta >= valorProduto:
    result = "Pode comprar o produto!"
else: 
    result = "Não tem saldo suficiente!"

print(result)
