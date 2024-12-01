ListaDeTarefas = [{"Nome": "Exemplo de Tarefa", "status": "pendente"}]

def AdicionarTarefa():
    Tarefa = input("Qual a tarefa deseja adicionar? ")
    ListaDeTarefas.append({"Nome": Tarefa, "status": "pendente"})

def MudarStatus():
    Tarefa = input("Quer mudar o status de qual tarefa? ")
    IndiceLista = 0
    for i in ListaDeTarefas:
        if i["Nome"] == Tarefa:
            ListaDeTarefas[IndiceLista]["status"] = "concluida"
            print(f"Tarefa '{Tarefa}' marcada como concluída!")
            return
        IndiceLista += 1
    print("Tarefa não encontrada.")

def MostrarTarefasPendentes():
    print("Tarefas pendentes:")
    for i in ListaDeTarefas:
        if i["status"] == "pendente":
            print(f"--> {i['Nome']}")

def MostrarTarefasConcluidas():
    print("Tarefas concluídas:")
    for i in ListaDeTarefas:
        if i["status"] == "concluida":
            print(f"--> {i['Nome']}")

def AlterarNomeTarefa():
    TarefaAtual = input("Qual o nome da tarefa que deseja alterar? ")
    for i in ListaDeTarefas:
        if i["Nome"] == TarefaAtual:
            NovoNome = input("Qual o novo nome da tarefa? ")
            i["Nome"] = NovoNome
            print(f"Tarefa atualizada para '{NovoNome}'")
            return
    print("Tarefa não encontrada.")

def ContarTarefasPendentes():
    count = sum(1 for i in ListaDeTarefas if i["status"] == "pendente")
    print(f"Você tem {count} tarefa(s) pendente(s).")

print("SISTEMA DE TAREFAS!")
while True:
    print("\nO que deseja fazer?")
    print("1 - Adicionar tarefa")
    print("2 - Mudar status de uma tarefa")
    print("3 - Ver tarefas pendentes")
    print("4 - Ver tarefas concluídas")
    print("5 - Alterar nome de uma tarefa")
    print("6 - Contar tarefas pendentes")
    print("0 - Sair")
    decisao = input("> ")

    if decisao == "1":
        AdicionarTarefa()
    elif decisao == "2":
        MudarStatus()
    elif decisao == "3":
        MostrarTarefasPendentes()
    elif decisao == "4":
        MostrarTarefasConcluidas()
    elif decisao == "5":
        AlterarNomeTarefa()
    elif decisao == "6":
        ContarTarefasPendentes()
    elif decisao == "0":
        print("Encerrando o sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
