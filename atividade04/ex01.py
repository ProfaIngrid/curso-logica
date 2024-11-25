jg1 = input("Jogador 1 \nDigite 1 - pedra, 2 - papel ou 3 - tesoura: ")
jg2 = input("Jogador 2 \nDigite 1 - pedra, 2 - papel ou 3 - tesoura: ")

#verifica empate
if jg1 == jg2:
    print("Empate")
#verifica jogador1
elif jg1 == "1" and jg2 == "3":
    print("Jogador 1 venceu!")
elif jg1 == "2" and jg2 == "1":
    print("Jogador 1 venceu!")
elif jg1 == "3" and jg2 == "2":
    print("Jogador 1 venceu!")
#verifca jogador2
else:
    print("Jogador 2 venceu!")
