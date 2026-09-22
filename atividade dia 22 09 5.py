prestacao_atual = float(input("Digite o valor da prestação atrasada: "))
taxa = float(input("Digite a taxa de juros: "))
dias = int(input("Digite o tempo de atraso em dias: "))

nova_prestacao = prestacao_atual + (prestacao_atual * taxa * dias) / 100

print("O valor da nova prestação é:", nova_prestacao)



