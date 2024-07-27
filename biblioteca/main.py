'''SISTEMA BIBLIOTECA'''
biblioteca = {}

def adicionar_livro(biblioteca, titulo, autor, genero):
    if titulo not in biblioteca:
        biblioteca[titulo] = {}
    biblioteca[titulo]['autor'] = autor
    biblioteca[titulo]['genero'] = genero

#depois de muito sofrer e ler artigos sobre dicionários em python, descobri que não se pode chamar uma chave que nao existe ainda :) foi traumatizante... 

def remover_livro(biblioteca, titulo):
    if titulo in biblioteca:
        del biblioteca[titulo]
        print('\nO livro foi removido.\n')
    else:
        print('\nO livro não foi encontrado.\n')

def buscar_livro(biblioteca, titulo):
        if titulo in biblioteca:
            print('\nO livro foi encontrado.\n')
        else:
            print('\nO livro não foi encontrado.\n')

def listar_livros(biblioteca, titulo):
    if biblioteca:
        for titulo in biblioteca.keys():
            print(titulo)
    else:
        print('A biblioteca está vazia, adicione alguk livro.\n')

def menu():
    return input('\nSISTEMA BIBLIOTECA\nEscolha a opção:\n [1]Adicionar livro na biblioteca\n [2]Remover livro da biblioteca\n [3]Buscar livro\n [4]Listar livros\n [5]Sair\n')

def main():
    while True:
        esc = menu()
        if esc == '1':    
            titulo = input('Por favor, digite o nome do exemplar: ')
            autor = input('Por favor, digite o nome do autor do livro: ')
            genero = input('Por favor, digite o gênero do livro: ')
            adicionar_livro(biblioteca, titulo, autor, genero)
            #queria muito tirar essas chaves do print, infelizmente fica pra proxima

        elif esc == '2':
            titulo = input('Qual exemplar deseja remover da biblioteca? ')
            remover_livro(biblioteca, titulo)
            print('Lista de livros da biblioteca: ', biblioteca)

        elif esc == '3':
            titulo = input('Qual livro deseja buscar? ')
            buscar_livro(biblioteca, titulo)

        elif esc == '4':
            print('Lista de livros da biblioteca: ')
            listar_livros(biblioteca, titulo)   

        elif esc == '5':
            print("ENCERRANDO PROGRAMA...\n")
            break

        else:
            print('OPÇÃO INVÁLIDA! Escolha outra opção, por favor.\n')

if __name__ == '__main__':
    main()
