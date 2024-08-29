'''SISTEMA DE BIBLIOTECA (CLASSES)'''

class Biblioteca:
    livros = []
    def __init__(self):
        pass

    def cadastro(self, nome, autor, ano):
        cad = {
            'Livro': nome,
            'Autor': autor,
            'Ano': ano,
            #'Disponibilidade': disponibilidade
        }
        self.livros.append(cad)
        #disponibilidade = True
        print(f'\nO LIVRO {nome} FOI CADASTRADO NA BIBLIOTECA.')
        pass

    def emprestimo(self, nome_dig):
        for cad in Biblioteca.livros:
            if cad['Livro'] == nome_dig:
                self.livros.remove(cad)
                print(f'\nLIVRO {nome_dig} REMOVIDO.')
                pass


def menu():
    return input('\n======================\nBIBLIOTECA\n======================\n[1]Cadastrar livro\n[2]Emprestar livro\n[3]Devolver livro\n[4]Ver o registro\n[5]Sair\nO QUE DESEJA FAZER? ')

def main():
    biblioteca = Biblioteca()
    while True:
        esc = menu()
        if esc == '1':
            nome = input('\nNOME DO LIVRO: ')
            autor = input('\nAUTOR DO LIVRO: ')
            ano = int(input('\nANO DO LIVRO: '))
            biblioteca.cadastro(nome, autor, ano)
            print(biblioteca.livros)

        elif esc == '2':
            nome_dig = input('\nQUAL LIVRO DESEJA FAZER EMPRÉSTIMO? ')
            biblioteca.emprestimo(nome_dig)
            print(biblioteca.livros)

        else:
            print('\nOPÇÃO INVÁLIDA.\n')

if __name__ == '__main__':
    main()
            
