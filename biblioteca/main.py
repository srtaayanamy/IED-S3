'''SISTEMA BIBLIOTECA'''
#ANNA JULIA DE SOUSA FÉLIX

biblioteca = {}

#declarando a biblioteca vazia pra depois ir preenchendo ela conforme a função abaixo:
#na função de adicionar livros, primeiro se faz a verificação se o livro já está na biblioteca e depois o adiciona na mesma com valores de autor e gênero
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

#aqui nas duas funções, tanto de remover quanto de buscar é verificado se o livro está na biblioteca, e caso esteja, ele é excluído ou dá o retorno de que foi encontrado.

def buscar_livro(biblioteca, titulo):
        if titulo in biblioteca:
            print('\nO livro foi encontrado.\n')
        else:
            print('\nO livro não foi encontrado.\n')

#em listar_livro tem a verificação se a biblioteca existe ou se está vazia e depois itera sobre cada titulo na biblioteca com o método keys, que é basicamente pra retornar a visualização das chaves no dicionário

def listar_livros(biblioteca, titulo):
    if biblioteca:
        for titulo in biblioteca.keys():
            print(titulo)
    else:
        print('A biblioteca está vazia, adicione alguk livro.\n')

#funções de menu com opções pro usuário escolher...

def menu():
    return input('\nSISTEMA BIBLIOTECA\nEscolha a opção:\n [1]Adicionar livro na biblioteca\n [2]Remover livro da biblioteca\n [3]Buscar livro\n [4]Listar livros\n [5]Sair\n')

def main():
#def main com laço while true pra ficar repetindo e acionando todas as funções pelo esc que veio num retorno da menu()
    while True:
        esc = menu()
        if esc == '1':    
            titulo = input('Por favor, digite o nome do exemplar: ')
            autor = input('Por favor, digite o nome do autor do livro: ')
            genero = input('Por favor, digite o gênero do livro: ')
            adicionar_livro(biblioteca, titulo, autor, genero)

        elif esc == '2':
            titulo = input('Qual exemplar deseja remover da biblioteca? ')
            remover_livro(biblioteca, titulo)
            print('Lista de livros da biblioteca: ', biblioteca)
            #queria muito tirar essas chaves do print, infelizmente fica pra proxima

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

#módulo pra executar o código diretamente

if __name__ == '__main__':
    main()
