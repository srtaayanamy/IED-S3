class Livro:
    livros = []
    def __init__(self):
        pass

    def adc_livro(self, titulo, autor, quant, preco):
        exemplar = {
            'Titulo': titulo,
            'Autor': autor,
            'Quantidade': quant,
            'Preço': preco
        }
        self.livros.append(exemplar)
        pass

    def adicionar_estoque(self, titulo_dig, quant_dig):
        for exemplar in Livro.livros:
            if exemplar['Titulo'] == titulo_dig:
                quant_atual = exemplar['Quantidade']
                quant_nova = quant_atual + quant_dig
                exemplar['Quantidade'] = quant_nova
                print(f'\nO LIVRO {titulo_dig} AGORA TEM {quant_nova} EXEMPLARES NO ESTOQUE\n')
                return
            else:
                print('\nO ESTOQUE NÃO FOI MODIFICADO\n')
                return
        print(f'\nO LIVRO {titulo_dig} NÃO FOI ENCONTRADO\n')


def menu():
    return input('\nLIVRARIA\n[1]Adicionar livro\n[2]Adicionar estoque\n')

def main():
    livro = Livro()
    while True:
        opc = menu()
        if opc == '1':
            titulo = input('NOME DO LIVRO: ')
            autor = input('AUTOR DO LIVRO: ')
            quant = int(input('QUANTIDADE DO LIVRO: '))
            preco = float(input('PREÇO DO LIVRO: '))
            livro.adc_livro(titulo, autor, quant, preco)
            print(livro.livros)

        elif opc == '2':
            titulo_dig = input('\nQUAL LIVRO DESEJA ADICIONAR MAIS NO ESTOQUE? ')
            quant_dig = int(input('QUANTOS EXEMPLARES DESEJA ADICIONAR? '))
            livro.adicionar_estoque(titulo_dig, quant_dig)

        elif opc == '3':
            print('\nENCERRANDO SISTEMA...\n')
            break
        else:
            print('\nOPÇÃO INVÁLIDA\n')

if __name__ == '__main__':
    main()



