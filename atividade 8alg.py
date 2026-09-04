def somar(numero1, numero2):
    return numero1 + numero2


def subtrair(numero1, numero2):
    return numero1 - numero2


def multiplicar(numero1, numero2):
    return numero1 * numero2


def dividir(numero1, numero2):
    if numero2 == 0:
        return None
    return numero1 / numero2


print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

operacao = input("Escolha uma operação: ")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operacao == "1":
    resultado = somar(numero1, numero2)
    print("Resultado:", resultado)
elif operacao == "2":
    resultado = subtrair(numero1, numero2)
    print("Resultado:", resultado)
elif operacao == "3":
    resultado = multiplicar(numero1, numero2)
    print("Resultado:", resultado)
elif operacao == "4":
    resultado = dividir(numero1, numero2)
    if resultado is None:
        print("Não é possível dividir por zero.")
    else:
        print("Resultado:", resultado)
else:
    print("Operação inválida.")