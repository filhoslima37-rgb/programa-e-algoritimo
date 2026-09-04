numero = int(input("Digite um número: "))
limite = int(input("Digite até qual número deseja a tabuada: "))

for multiplicador in range(1, limite + 1):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
