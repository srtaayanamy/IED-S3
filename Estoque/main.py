'''Sistema de estoque'''

#O sistema deve permitir ao usuário adicionar, remover, atualizar, visualizar todos e por ID, filtrar produtos e gerar relatorio dos produtos no estoque. 

def adc_produto(produtos, id_ant, nome, quantidade, preco):
    id_prod = id_ant + 1
    produto = {
        'id': id_prod,
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }
    produtos.append(produto)
    print(f'O produto "{nome}" foi adicionado!')
    return id_prod

def rem_produto(produtos, id_prod):
    for produto in produtos:
        if produto['id'] == id_prod:
            produtos.remove(produto)
            print('\nProduto removido do estoque!\n')
            return
    print('Produto não encontrado.\n')

def atu_produto(produtos, opc):
    if opc == '1':
        nome = input('Qual o produto que deseja alterar o nome? ')
        for produto in produtos:
            if produto['nome'] == nome:
                novo_nome = input('Qual nome deseja inserir no lugar? ')
                produto['nome'] = novo_nome
                print('\nNome alterado com sucesso!\n')

    elif opc == '2':
        nome = input('Qual o produto que deseja alterar a quantidade? ')
        for produto in produtos:
            if produto['nome'] == nome:
                nova_quantidade = int(input('Qual a nova quantidade? '))
                produto['quantidade'] = nova_quantidade
                print('\nQuantidade alterada com sucesso!\n')

    elif opc == '3':
        nome = input('Qual o produto que deseja alterar o preço? ')
        for produto in produtos:
            if produto['nome'] == nome:
                novo_preco = float(input('Qual o novo preço? '))
                produto['preco'] = novo_preco
                print('\nPreço alterado com sucesso!\n')

def ver_produtos(produtos):
    if produtos:
        for produto in produtos:
            print(produto)
    else:
        print('\nO estoque está vazio.\n')

def pes_produto(produtos, id_prod):
    for produto in produtos:
        if produto['id'] == id_prod:
            print(produto)
            return
    print('\nCódigo não encontrado.\n')

def fil_produtos(produtos, fil_quantidade, opc_fil):
    fil_quantidade = []
    if opc_fil == '1':
        quantidade = int(input('Por que quantidade deseja filtrar? '))
        for produto in produtos:
            if produto['quantidade'] == quantidade:
                fil_quantidade.append(produto)
    
    elif opc_fil == '2':
        preco = float(input('Por que preço deseja filtrar? '))
        for produto in produtos:
            if produto['preco'] == preco:
                fil_quantidade.append(produto)

    if fil_quantidade:
        for produto in fil_quantidade:
            print(produto)
    else:
        print('\nNão foi possivel filtrar\n')

def rel_produtos():
    pass

def menu():
    return input('\n O QUE DESEJA FAZER?\n[1]Adicionar produto\n[2]Remover produto\n[3]Atualizar produto\n[4]Visualizar produtos\n[5]Filtrar produtos\n[6]Relatório dos produtos\n[7]Pesquisar produto\n[8]Sair\n')

def main():
    id_ant = 0
    produtos = []
    while True:
        esc = menu()
        if esc == '1':
            nome = input('Nome do produto: ')
            quantidade = int(input('Quantidade do produto: '))
            preco = float(input('Preço do produto: '))
            id_ant = adc_produto(produtos, id_ant, nome, quantidade, preco)

        elif esc == '2':
            id_prod = int(input('ID do produto a ser removido: '))
            rem_produto(produtos, id_prod)

        elif esc == '3':
            opc = input('\n O QUE VOCÊ DESEJA EDITAR?\n[1]Nome de um produto\n[2]Quantidade de um produto\n[3]Preço de um produto\n')
            atu_produto(produtos, opc)

        elif esc == '4':
            print('\nESTOQUE DE PRODUTOS!!!\n')
            ver_produtos(produtos)

        elif esc == '5':
            opc_fil = input('\n VOCÊ DESEJA FILTRAR POR QUE TIPO?\n[1]Quantidade\n[2]Preço\n')
            fil_produtos(produtos, quantidade, opc_fil)

        elif esc == '6':
            pass

        elif esc == '7':
            id_prod = int(input('Qual código deseja buscar? '))
            pes_produto(produtos, id_prod)

        elif esc == '8':
            print('\nENCERRANDO SISTEMA...')
            break

        else:
            print('\nOPÇÃO INVÁLIDA. Escolha outra opção.')

if __name__ == '__main__':
    main()