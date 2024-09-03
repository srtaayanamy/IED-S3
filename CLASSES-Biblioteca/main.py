'''SISTEMA DE BIBLIOTECA (CLASSES)'''

class Biblioteca:
    livros = []
    emprestados = []
    def __init__(self):
        pass

    def cadastro(self, nome, autor, ano):
        cad = {
            'Livro': nome,
            'Autor': autor,
            'Ano': ano,
            'Disponibilidade': True
        }
        self.livros.append(cad)
        print(f'O LIVRO {nome} FOI CADASTRADO NA BIBLIOTECA.')
        pass

    def emprestimo(self, nome_dig):
        for cad in Biblioteca.livros:
            if cad['Livro'] == nome_dig:
                if cad['Disponibilidade']:
                    cad['Disponibilidade'] = False
                    self.livros.remove(cad)
                    self.emprestados.append(cad)
                    print(f'\nLIVRO {nome_dig} EMPRESTADO.')
                    return
                else:
                    print(f'\nO LIVRO "{nome_dig}" JÁ ESTÁ EMPRESTADO.')
                    return
        print(f'\nO LIVRO {nome_dig} NÃO ESTÁ NA BIBLIOTECA.')

    def devolucao(self, nome_dig):
        for cad in Biblioteca.emprestados:
            if cad['Livro'] == nome_dig:
                cad['Disponibilidade'] = True
                self.emprestados.remove(cad)
                self.livros.append(cad)
                print(f'\nO LIVRO {nome_dig} FOI DEVOLVIDO.')
                return
        print(f'\nO LIVRO {nome_dig} NÃO ESTÁ EMPRESTADO.')

    def registro(self):
        if not self.emprestados:
            print('\nNÃO HÁ LIVROS EMPRESTADOS NO MOMENTO.')
        else:
            print('\nLIVROS EMPRESTADOS NO MOMENTO:')
            print(self.emprestados)


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
            print('\nLIVROS DISPONÍVEIS NA BIBLIOTECA:')
            print(biblioteca.livros)

        elif esc == '2':
            nome_dig = input('\nQUAL LIVRO DESEJA FAZER EMPRÉSTIMO? ')
            biblioteca.emprestimo(nome_dig)
            print('\nLIVROS DISPONÍVEIS NA BIBLIOTECA:')
            print(biblioteca.livros)

        elif esc == '3':
            nome_dig = input('\nQUAL LIVRO DESEJA DEVOLVER? ')
            biblioteca.devolucao(nome_dig)
            print('\nLIVROS DISPONÍVEIS NA BIBLIOTECA:')
            print(biblioteca.livros)

        elif esc == '4':
            biblioteca.registro()

        elif esc == '5':
            print('\nENCERRANDO SISTEMA...\n')
            break

        else:
            print('\nOPÇÃO INVÁLIDA.\n')

if __name__ == '__main__':
    main()
