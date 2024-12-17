tarefas = []

def exibir_tarefas(tarefas_filtradas):
    if not tarefas_filtradas:
        print("Não há tarefas encontradas.")
    else:
        for i, tarefa in enumerate(tarefas_filtradas, 1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i}. {tarefa['nome']} - {status} - Prioridade: {tarefa['prioridade']} - Categoria: {tarefa['categoria']}")


def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefas.append({
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    })
    print(f"Tarefa '{nome}' adicionada com sucesso!")


def listar_tarefas():
    exibir_tarefas(tarefas)

def marcar_concluida(indice):
    if 0 < indice <= len(tarefas):
        tarefas[indice - 1]["concluida"] = True
        print(f"Tarefa '{tarefas[indice - 1]['nome']}' marcada como concluída.")
    else:
        print("Tarefa não encontrada.")


def exibir_por_prioridade(prioridade):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["prioridade"] == prioridade]
    exibir_tarefas(tarefas_filtradas)


def exibir_por_categoria(categoria):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["categoria"] == categoria]
    exibir_tarefas(tarefas_filtradas)


def menu():
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Exibir tarefas por prioridade")
        print("5. Exibir tarefas por categoria")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade (baixa, média, alta): ")
            categoria = input("Categoria: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            try:
                indice = int(input("Número da tarefa a ser marcada como concluída: "))
                marcar_concluida(indice)
            except ValueError:
                print("Por favor, insira um número válido.")

        elif opcao == "4":
            prioridade = input("Informe a prioridade (baixa, média, alta): ")
            exibir_por_prioridade(prioridade)

        elif opcao == "5":
            categoria = input("Informe a categoria: ")
            exibir_por_categoria(categoria)

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
