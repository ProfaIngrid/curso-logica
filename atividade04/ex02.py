num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

print("Qual a operação?")
operacao = input("Escolha -> + | - | * | / :")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2 
    else: 
        resultado = "Operação inválida!"
else:
    resultado = "Operação inválida!"

print(resultado)

