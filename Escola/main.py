def adc_aluno(alunos, nome, idade, mat, port, hist, turma):
    aluno = {
        'matriculas' : {
            'nome': nome,
            'idade': idade,
            'notas': {
                'matematica': mat, 'portugues': port, 'historia': hist},
            'turma': turma
        }
    }

    alunos.append(aluno)

def adc_turma(escola, turma):
    if turma not in escola:
        escola[turma] = []
    else:
        print('\nEssa turma já existe.\n')


def menu():
    return input('\nO QUE DESEJA FAZER?\n\n[1]Adicionar aluno\n[2]Adicionar turma\n[3]Adicionar aluno á turma\n[4]Listar alunos\n[5]Gerar boletim individual\n[6]Gerar boletim por turma\n[7]Sair\n')

def main():
    alunos = []
    escola = {}
    while True:
        esc = menu()
        if esc == '1':
            nome = input('Nome do aluno: ')
            idade = input('Idade do aluno: ')
            turma = input('Turma do aluno: ')
            mat = input('Nota em matemática: ')
            port = input('Nota em português: ')
            hist = input('Nota em história: ')
            adc_aluno(alunos, nome, idade, mat, port, hist, turma)

        elif esc == '2':
            turma = input('Nome da turma: ')
            adc_turma(escola, turma)

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
