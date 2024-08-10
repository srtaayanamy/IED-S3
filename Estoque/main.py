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
    print(f'O PRODUTO "{nome}" FOI ADICIONADO!')
    return id_prod

def rem_produto(produtos, id_prod):
    for produto in produtos:
        if produto['id'] == id_prod:
            produtos.remove(produto)
            print('\nPRODUTO REMOVIDO DO ESTOQUE!\n')
            return
    print('PRODUTO NÃO ENCONTRADO.\n')

def atu_produto(produtos, opc):
    if opc == '1':
        nome = input('QUAL O PRODUTO QUE DESEJA ALTERAR O NOME? ')
        for produto in produtos:
            if produto['nome'] == nome:
                novo_nome = input('QUAL NOME DESEJA INSERIR NO LUGAR? ')
                produto['nome'] = novo_nome
                print('\nNOME ALTERADO COM SUCESSO!\n')

    elif opc == '2':
        nome = input('QUAL O PRODUTO QUE DESEJA ALTERAR A QUANTIDADE? ')
        for produto in produtos:
            if produto['nome'] == nome:
                nova_quantidade = int(input('QUAL A NOVA QUANTIDADE? '))
                produto['quantidade'] = nova_quantidade
                print('\nQUANTIDADE ALTERADA COM SUCESSO!\n')

    elif opc == '3':
        nome = input('QUAL O PRODUTO QUE DESEJA ALTERAR O PREÇO? ')
        for produto in produtos:
            if produto['nome'] == nome:
                novo_preco = float(input('QUAL O NOVO PREÇO? '))
                produto['preco'] = novo_preco
                print('\nPREÇO ALTERADO COM SUCESSO!\n')

def ver_produtos(produtos):
    if produtos:
        for produto in produtos:
            print(produto)
    else:
        print('\nO ESTOQUE ESTÁ VAZIO.\n')

def pes_produto(produtos, id_prod):
    for produto in produtos:
        if produto['id'] == id_prod:
            print(produto)
            return
    print('\nCÓDIGO NÃO ENCONTRADO.\n')

def fil_produtos(produtos, fil_quantidade, opc_fil):
    fil_quantidade = []
    if opc_fil == '1':
        quantidade = int(input('POR QUE QUANTIDADE DESEJA FILTRAR? '))
        for produto in produtos:
            if produto['quantidade'] == quantidade:
                fil_quantidade.append(produto)
    
    elif opc_fil == '2':
        preco = float(input('\nPOR QUE PREÇO DESEJA FILTRAR? \n'))
        for produto in produtos:
            if produto['preco'] == preco:
                fil_quantidade.append(produto)

    if fil_quantidade:
        print('\nPRODUTOS FILTRADOS:')
        for produto in fil_quantidade:
            print(produto)
    else:
        print('\nNÃO FOI POSSIVEL FILTRAR\n')

def rel_produtos(produtos):
    if not (produtos):
        print('\nO ESTOQUE ESTÁ VAZIO.\n')
        return
    total_estoque = 0
    for produto in produtos:
        print(produto)
        total_estoque = total_estoque + produto['quantidade'] * produto['preco']
        print(f'\nVALOR TOTAL DO ESTOQUE: (até agora) R$ {total_estoque:.2f}\n')

def menu():
    return input('\n O QUE DESEJA FAZER?\n\n[1]Adicionar produto\n[2]Remover produto\n[3]Atualizar produto\n[4]Visualizar produtos\n[5]Filtrar produtos\n[6]Relatório dos produtos\n[7]Pesquisar produto\n[8]Sair\n\n')

def main():
    id_ant = 0
    produtos = []
    while True:
        esc = menu()
        if esc == '1':
            nome = input('NOME DO PRODUTO: ')
            quantidade = int(input('QUANTIDADE DO PRODUTO: '))
            preco = float(input('PREÇO DO PRODUTO: '))
            id_ant = adc_produto(produtos, id_ant, nome, quantidade, preco)

        elif esc == '2':
            id_prod = int(input('ID DO PRODUTO A SER REMOVIDO: '))
            rem_produto(produtos, id_prod)

        elif esc == '3':
            opc = input('\n O QUE VOCÊ DESEJA EDITAR?\n[1]Nome de um produto\n[2]Quantidade de um produto\n[3]Preço de um produto\n')
            atu_produto(produtos, opc)

        elif esc == '4':
            print('\nESTOQUE DE PRODUTOS!!!\n')
            ver_produtos(produtos)

        elif esc == '5':
            opc_fil = input('\n VOCÊ DESEJA FILTRAR POR QUE TIPO?\n[1]Quantidade\n[2]Preço\n\n')
            fil_produtos(produtos, quantidade, opc_fil)

        elif esc == '6':
            print('\nRELATÓRIO DOS PRODUTOS:\n')
            rel_produtos(produtos)

        elif esc == '7':
            id_prod = int(input('QUAL CÓDIGO DESEJA BUSCAR? '))
            pes_produto(produtos, id_prod)

        elif esc == '8':
            print('\nENCERRANDO SISTEMA...')
            break

        else:
            print('\nOPÇÃO INVÁLIDA. Escolha outra opção.')

if __name__ == '__main__':
    main()
