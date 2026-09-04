frase = input("Digite uma frase: ").lower()

contagem_a = 0
contagem_e = 0
contagem_i = 0
contagem_o = 0
contagem_u = 0

for caractere in frase:
    if caractere in "a":
        contagem_a += 1
    elif caractere in "e":
        contagem_e += 1
    elif caractere in "i":
        contagem_i += 1
    elif caractere in "o":
        contagem_o += 1
    elif caractere in "u":
        contagem_u += 1

total = contagem_a + contagem_e + contagem_i + contagem_o + contagem_u

print("Total de vogais:", total)
print("a:", contagem_a)
print("e:", contagem_e)
print("i:", contagem_i)
print("o:", contagem_o)
print("u:", contagem_u)
