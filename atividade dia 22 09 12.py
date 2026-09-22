raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

pi = 3.14
area_base = pi * raio ** 2
area_lateral = 2 * pi * raio * altura
area_total = 2 * area_base + area_lateral

print("A área total do cilindro é:", area_total)



