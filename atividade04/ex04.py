val1 = float(input("Digite o 1º lado do triângilo: "))
val2 = float(input("Digite o 2º lado do triângilo: "))
val3 = float(input("Digite o 3º lado do triângilo: "))

if val1 <= 0 or val2 <= 0 or val3 <= 0:
    print("Não é um triângulo")
elif val1 == val2 == val3:
    print("Triângulo Equilátero")
elif val1 != val2 != val3:
    print("Triangulo Escaleno")
elif val1 == val2 or val1 == val3 or val2 == val3:
    print("Triangulo Isósceles")
elif val1 + val2 > val3 and val2 + val3 > val1 and val1 + val3 > val2:
    print("Não é um triângulo")


