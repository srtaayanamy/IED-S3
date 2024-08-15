def adc_aluno(alunos, nome, idade, mat, port, hist, art, fil, turma):
    aluno = {
        'matriculas' : {
            'nome': nome,
            'idade': idade,
            'notas': {
                'matematica': mat, 'portugues': port, 'historia': hist, 'artes': art, 'filosofia': fil},
            'turma': turma
        }
    }

    turmas = {
        '1A': [],
        '1B': [],
        }
    
    alunos.append(aluno)

def menu():
    return input('\nO QUE DESEJA FAZER?\n\n[1]Adicionar aluno\n[2]Adicionar turma\n[3]Adicionar aluno á turma\n[4]Listar alunos\n[5]Gerar boletim individual\n[6]Gerar boletim por turma\n[7]Sair\n')

def main():
    alunos = []
    while True:
        esc = menu()
        if esc == '1':
            pass
        elif esc == '2':
            pass
        elif esc == '3':
            pass
        elif esc == '4':
            pass
        elif esc == '5':
            pass
        elif esc == '6':
            pass
        elif esc == '7':
            print('\nENCERRANDO SISTEMA...\n')
        else: 
            print('\nOPÇÃO INVÁLIDA. Escolha outra opção.\n')
         
if __name__ == '__main__':
    main()