'''Sistema de biblioteca MELHORADO'''

def adc_livro(livros, id_ant, titulo, autor, genero):
    id_atual = id_ant + 1
    livro = {
        'id': id_atual,
        'titulo': titulo,
        'autor': autor,
        'genero': genero
    }
    livros.append(livro)
    print(f'\nO LIVRO {titulo} FOI ADICIONADO NA BIBLIOTECA!\n')
    return id_atual

def rem_livro(livros, livro_dig):
    for livro in livros:
        if livro['titulo'] == livro_dig:
            livros.remove(livro)
            print(f'\nLIVRO {livro_dig} REMOVIDO\n')
            return
    print('\nO LIVRO NÃO FOI ENCONTRADO\n')

def bus_livro(livros, livro_dig):
    for livro in livros:
        if livro['titulo'] == livro_dig:
            print(f'\nO LIVRO {livro_dig} FOI ENCONTRADO NA BIBLIOTECA!\n')
            return
    print('\nO LIVRO NÃO FOI ENCONTRADO\n')

def lis_livros(livros):
    if not livros:
        print('\nA BIBLIOTECA ESTÁ VAZIA\n')
    else:
        for livro in livros:
            print(f"{livro['id']} - {livro['titulo']} | Autor: {livro['autor']} | Gênero: {livro['genero']}")

def menu():
    return input('\n======================\nO QUE DESEJA FAZER?\n======================\n[1]Adicionar livro\n[2]Remover livro\n[3]Buscar livro\n[4]Listar livros\n[5]Sair\n')

def main():
    id_ant = 0
    livros = []
    while True:
        esc = menu()
        if esc == '1':
            titulo = input('TITULO DO LIVRO: ')
            autor = input('AUTOR DO LIVRO: ')
            genero = input('GENERO DO LIVRO: ')
            id_ant = adc_livro(livros, id_ant, titulo, autor, genero)
        elif esc == '2':
            livro_dig = input('\nQUE LIVRO DESEJA REMOVER? ')
            rem_livro(livros, livro_dig)
        elif esc == '3':
            livro_dig = input('\nQUAL LIVRO DESEJA BUSCAR? ')
            bus_livro(livros, livro_dig)
        elif esc == '4':
            lis_livros(livros)
        elif esc == '5':
            print('\nENCERRANDO SISTEMA...\n')
            break
        else:
            print('\nOPÇÃO INVÁLIDA\n')

if __name__ == '__main__':
    main()
