'''Sistema da Escola'''

def adc_aluno(alunos, matricula, nome, idade, turma):
    mat_atual = matricula + 1
    aluno = {
        'matricula': mat_atual,
        'nome': nome,
        'idade': idade, 
        'turma': turma, 
        'notas': {}
    }
    alunos.append(aluno)
    print('\nALUNO ADICIONADO NA ESCOLA.\n')
    return mat_atual

def adc_turma(turmas, turma_dig):
    if turma_dig not in turmas:
        turmas[turma_dig] = []
        print('\nA TURMA FOI ADICIONADA NA ESCOLA.\n')
    else:
        print('\nA TURMA NÃO FOI ADICIONADA NA ESCOLA\n')

def lis_turmas(alunos, turma_dig):
    for aluno in alunos:
        if aluno['turma'] == turma_dig:
            print(aluno)
        else:
            print('\nTURMA INVÁLIDA.')

def adc_notas(alunos, nome_dig):
    for aluno in alunos:
        if aluno['nome'] == nome_dig:
            materia = input('QUAL A MATÉRIA? ')
            nota = float(input('\nNOTA: '))
            aluno['notas'][materia] = nota
            print('\nNOTA ADICIONADA!\n')
        else:
            print('\nNOTA NÃO ADICIONADA\n')

def med_aluno(alunos, nome_dig):
    total = 0
    for aluno in alunos:
        if aluno['nome'] == nome_dig:
            for nota in aluno['notas'].values():
                total = total + nota
            media = total / len(aluno['notas'])
            print('\nA MÉDIA É: ', media, '\n')
            return
    print('\nNÃO FOI POSSIVEL CALCULAR A MÉDIA.\n')

def med_turma(alunos, turma_dig):
    total = 0
    i = 0
    for aluno in alunos:
        if aluno['turma'] == turma_dig:
            if aluno['notas']:
                for nota in aluno['notas'].values():
                    total = total + nota
                    i = i + len(aluno['notas'])
    if i > 0:
        media = total / i
        print('\nA MÉDIA É: ', media, '\n')
    else:
        print('\nNÃO FOI POSSIVEL CALCULAR A MÉDIA.\n')

def bol_individual(alunos, nome_dig):
    for aluno in alunos:
        if aluno['nome'] == nome_dig:
                print('\nBOLETIM DE', {aluno['nome']},':\n')
                for materia, nota in aluno['notas'].items():
                    print(f"{materia}: {nota}")
                media = med_aluno(alunos, nome_dig)
                if media is not None:
                    print('A MÉDIA É: ', media, '\n')
                    return
                
def bol_turma(alunos, turma_dig):
    lis_turmas(alunos, turma_dig)
    med_turma(alunos, turma_dig)

def menu():
    return input('\n==================\nSISTEMA DA ESCOLA\n==================\nESCOLHA O QUE DESEJA FAZER:\n[1]Adicionar aluno\n[2]Adicionar turma na escola\n[3]Adicionar notas de um aluno\n[4]Listar alunos por turma\n[5]Calcular a média de um aluno\n[6]Calcular média de uma turma\n[7]Gerar boletim individual\n[8]Gerar boletim de turma\n[9]Sair\n')

def main():
    matricula = 0
    alunos = []
    turmas = {}
    while True:
        esc = menu()
        if esc == '1':
            nome = input('\nNOME DO ALUNO: ')
            idade = input('\nIDADE DO ALUNO: ')
            turma = input('\nTURMA DO ALUNO: ')
            if turma not in turmas:
                print('\nESSA TURMA NÃO EXISTE. Adicione ela na escola primeiro.\n')
            else:
                matricula = adc_aluno(alunos,matricula, nome, idade, turma)

        elif esc == '2':
            turma_dig = input('\nNOME DA TURMA: ')
            adc_turma(turmas, turma_dig)

        elif esc == '3':
            aluno_dig = input('\nQUAL ALUNO DESEJA ADICIONAR NOTAS? ')
            adc_notas(alunos, aluno_dig)

        elif esc == '4':
            turma_dig = input('\nQUAL TURMA DESEJA LISTAR OS ALUNOS? ')
            print(f'\nTURMA {turma_dig}:\n')
            lis_turmas(alunos, turma_dig)

        elif esc == '5':
            aluno_dig = input('\nQUAL ALUNO DESEJA VER A MÉDIA? ')
            med_aluno(alunos, aluno_dig)

        elif esc == '6':
            turma_dig = input('\nQUE TURMA DESEJA VER A MÉDIA? ')
            med_turma(alunos, turma_dig)

        elif esc == '7':
            nome_dig = input('\nQUAL ALUNO DESEJA VER O BOLETIM? ')
            bol_individual(alunos, nome_dig)

        elif esc == '8':
            turma_dig = input('\nQUAL A TURMA? ')
            print('\nRELATÓRIO DA TURMA', {turma_dig},':\n')
            bol_turma(alunos, turma_dig)

        elif esc == '9':
            print('\nENCERRANDO SISTEMA...\n')
            break

        else:
            print('\nOPÇÃO INVÁLIDA. Escolha outra opção.\n')

if __name__ == '__main__':
    main()
