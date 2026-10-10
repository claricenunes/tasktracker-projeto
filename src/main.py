from datetime import datetime

tarefas = []


def ler_titulo():
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório. Tente novamente.")


def ler_prioridade():
    prioridades = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa",
    }

    while True:
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if prioridade in prioridades:
            return prioridades[prioridade]
        print("Erro: informe Alta, Média ou Baixa.")


def ler_data_limite():
    while True:
        data = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Erro: data inválida. Use o formato DD/MM/AAAA.")


def cadastrar_tarefa():
    print("\n--- Cadastrar nova tarefa ---")
    titulo = ler_titulo()
    descricao = input("Descrição da tarefa: ").strip()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f'Tarefa "{titulo}" cadastrada com sucesso!')


def visualizar_tarefas():
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Não existem tarefas cadastradas.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f'Título: {tarefa["titulo"]}')
        print(f'Descrição: {tarefa["descricao"] or "Não informada"}')
        print(f'Prioridade: {tarefa["prioridade"]}')
        print(f'Data limite: {tarefa["data_limite"]}')
        print(f'Status: {tarefa["status"]}')

    concluidas = sum(1 for tarefa in tarefas if tarefa["status"] == "Concluída")
    print(f"\nTotal de tarefas concluídas: {concluidas}")


def concluir_tarefa():
    if not tarefas:
        print("\nNão existem tarefas cadastradas para concluir.")
        return

    visualizar_tarefas()
    entrada = input("\nDigite o número da tarefa que deseja concluir: ").strip()

    try:
        numero = int(entrada)
    except ValueError:
        print("Erro: digite um número válido.")
        return

    if numero < 1 or numero > len(tarefas):
        print("Tarefa não encontrada.")
        return

    tarefa = tarefas[numero - 1]
    if tarefa["status"] == "Concluída":
        print("Essa tarefa já está concluída.")
        return

    tarefa["status"] = "Concluída"
    print(f'Tarefa "{tarefa["titulo"]}" marcada como concluída!')


def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 3.")


if __name__ == "__main__":
    main()
