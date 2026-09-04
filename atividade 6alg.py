quantidade = int(input("Quantos números deseja informar? "))

while quantidade <= 0:
    print("A quantidade deve ser maior que zero.")
    quantidade = int(input("Digite uma quantidade válida: "))

numeros = []

for indice in range(quantidade):
    numero = float(input(f"Digite o {indice + 1}º número: "))
    numeros.append(numero)

media = sum(numeros) / quantidade

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Média:", media)
