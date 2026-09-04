import random

numero_secreto = random.randint(1, 100)
tentativas = 0
palpite = 0

print("Tente adivinhar o número entre 1 e 100!")

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número secreto é maior.")
    elif palpite > numero_secreto:
        print("O número secreto é menor.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
