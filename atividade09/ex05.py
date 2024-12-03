#Crie um programa que leia uma string fornecida pelo usuário e, 
# utilizando um laço for, conte quantas vogais (a, e, i, o, u) existem 
# nessa string. O programa deve imprimir o total de vogais encontradas.

palavra = input("Digite uma palavra: ")
a = 0
e = 0
i = 0
o = 0
u = 0
c = 0

for letra in palavra:
    if letra.lower() == 'a':
        a = a + 1
    elif letra.lower() == 'e':
        e = e +1 
    elif letra.lower() == 'i':
        i = i +1
    elif letra.lower() == 'o':
        o = o + 1
    elif letra.lower() == 'u':
        u = u + 1
    else:
        c = c + 1 
print(f"Foram encontras:\n A:{a} \n E:{e} \n I:{i} \n O:{o} \n U:{u} \n Consoantes:{c}")

