'''SISTEMA BIBLIOTECA'''

biblioteca = {}

def adicionar_livro(biblioteca, titulo, autor, genero):
    if titulo not in biblioteca.keys():
        biblioteca[titulo] = {}
    biblioteca[titulo]['autor'] = autor
    biblioteca[titulo]['genero'] = genero

#depois de muito sofrer e ler artigos sobre dicionários em python, descobri que nao se pode chamar uma chave que nao existe ainda :) foi traumatizante... 

#ai eu pensei que deveria ter algo pra verificar e coloquei o .keys, mas não sei se é a melhor maneira pra verificar pq n lembro de vc ter comentado sobre outra e aparentemente funciona, mas qualquer coisa eu mudo depois.

def remover_livro(titulo, biblioteca):
    #dando erro aqui
    if titulo in biblioteca.keys():
        del biblioteca[titulo]
    else:
        print('O livro não foi encontrado.\n')


def menu():
    return input('SISTEMA BIBLIOTECA\nEscolha a opção:\n [1]Adicionar livro na biblioteca.\n [2]Remover livro da biblioteca.\n [3]Buscar livro\n [4]Listar livros\n [5]Sair\n')

def main():
    while True:
        esc = menu()
        if esc == '1':    
            titulo = input('Por favor, digite o nome do exemplar: ')
            autor = input('Por favor, digite o nome do autor do livro: ')
            genero = input('Por favor, digite o gênero do livro: ')
            adicionar_livro(biblioteca, titulo, autor, genero)
            #queria muito tirar essas chaves do print, infelizmente fica pra proxima
            print(biblioteca)

        elif esc == '2':
            titulo = input('Qual exemplar deseja remover da biblioteca? ')
            remover_livro(biblioteca, titulo)

        elif esc == '5':
            print("ENCERRANDO PROGRAMA...\n")
            break

        else:
            print('OPÇÃO INVÁLIDA! Escolha outra opção, por favor.\n')

if __name__ == '__main__':
    main()