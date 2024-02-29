# Aplicação Prática 1: Desenvolver em sala: Criarem uma lista de tarefas para um dia e escrever um script que adicione, remova e altere tarefas.

tarefas = []
#declaração das funçoes de adicionar,remover,alterar e exibir
def criar_item(lista_tarefas, item):
    lista_tarefas.append(item)
    print('Item adicionado! \n')

def remover_item(lista_tarefas, item):
    if item in lista_tarefas:
        lista_tarefas.remove(item)
        print('Item removido! \n')
    else:
        print('Item não encontrado. \n')

def alterar_item(lista_tarefas, item_nov, item_ant):
    for i in range(len(lista_tarefas)):
        if lista_tarefas[i] == item_ant:
            lista_tarefas[i] = item_nov
            return lista_tarefas
    print('Item não encontrado.')
#obs-> parte de alterar e exibir foi bem mais complicado pra mim que o resto :(
def exibir_lista(tarefas):
    if tarefas:
        print("Lista de tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            # enumerate retorna um objeto enumerado que contém pares de índice e valor
            #f"{i}. {tarefa}" --> f mostra q é string
            print(f"{i}. {tarefa}")
    else:
        print("Lista vazia.")

while True:
#area da função principal
    print('1-Criar tarefa;')
    print('2-Remover tarefa;')
    print('3-Substituir tarefa;')
    print('4-Exibir a lista;')
    print('5-Sair;')

    esc = input('Escolha uma opção:')
#opçoes direcionadas a cada função
    if esc == '1':
        item = input('Digite o item que quer adicionar: \n')
        criar_item(tarefas, item)
    elif esc == '2':
        item = input('Digite o item que quer remover: \n')
        remover_item(tarefas, item)
    elif esc == '3':
        item_ant = input('Digite o item que quer substituir: \n')
        item_nov = input('Digite o novo item: \n')
        alterar_item(tarefas, item_nov, item_ant)
    elif esc == '4':
        exibir_lista(tarefas)
    elif esc == '5':
        break
    else:
        print('Opção inválida!')
        