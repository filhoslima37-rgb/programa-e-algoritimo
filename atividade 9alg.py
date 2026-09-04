while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")

        with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(tarefa + "\n")

        print("Tarefa adicionada com sucesso.")

    elif opcao == "2":
        try:
            with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
                tarefas = arquivo.readlines()

            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("\nLista de tarefas:")
                for numero, tarefa in enumerate(tarefas, start=1):
                    print(f"{numero}. {tarefa.strip()}")

        except FileNotFoundError:
            print("Nenhuma tarefa cadastrada.")

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")