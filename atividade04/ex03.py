idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Entrada Liberada!")
elif idade >= 16 or idade <= 17: 
    acompanhado = input("Possui acompanhante? ")
    if acompanhado == "sim":
        print("Entrada Liberada!")
    else:
        print("Entrada Negada")
else:
    print("Entrada Negada")
