'''Sistema de hotelaria'''
#adicionar reservas, cancelar reservas, buscar reservas pelo nome do hóspede e listar todas as reservas.

#colocar a verificação de datas e quartos 

def adc_reserva(reservas, id_ant, nome, numero, checkin, checkout):
        id_res = id_ant + 1
        reserva = {
            'id' : id_res,
            'nome' : nome,
            'numero' : numero,
            'checkin' : checkin,
            'checkout' : checkout
        }
        reservas.append(reserva)
        print('\nReserva de número {} feita!\n'.format(id_res))
        return id_res

def can_reservas(reservas, id_res):
    for reserva in reservas:
        if reserva['id'] == id_res:
            reservas.remove(reserva)
            print('\nReserva de número {} foi cancelada.\n' .format(id_res))
            return
    print('\nReserva não encontrada.\n')

def bus_reservas(reservas, nome):
    for reserva in reservas:
        if reserva['nome'] == nome:
            print('\nReserva no nome de {} foi encontrada.\n' .format(nome))
            return
    else:
        print('\nReserva não encontrada.\n')

def lis_reservas(reservas):
    for reserva in reservas:
        print(reserva)

def edi_reservas(reservas, opc):
    if opc == '1':
        nome = input('\nQual o nome que deseja editar?\n')
        for reserva in reservas:
            if reserva['nome'] == nome:
                novo_nome = input('\nDigite o novo nome do cliente: \n')
                reserva['nome'] = novo_nome 
                print('\nNome alterado com sucesso!\n')

    elif opc == '2':
        nome = input('\nDigite o cliente que você deseja editar o quarto: \n')
        for reserva in reservas:
            if reserva['nome'] == nome:
                novo_numero = input('\nDigite o novo quarto do cliente: \n')
                reserva['numero'] = novo_numero
                print('\nQuarto alterado com sucesso!')

    elif opc == '3':
        nome = input('\nDigite o cliente que você deseja editar o checkin: \n')
        for reserva in reservas:
            if reserva['nome'] == nome:
                novo_checkin = input('\nDigite o novo checkin: \n')
                reserva['checkin'] = novo_checkin
                print('\nCheckin alterado com sucesso!')

    elif opc == '4':
        nome = input('\nDigite o cliente que você deseja editar o checkout: \n')
        for reserva in reservas:
            if reserva['nome'] == nome:
                novo_checkout = input('\nDigite o novo checkout: \n')
                reserva['checkout'] = novo_checkout
                print('\nCheckout alterado com sucesso!')

    else:
        print('\nOPÇÃO INVÁLIDA. Escolha outra opção.')

def menu():
    return input('\n O QUE DESEJA FAZER?\n[1]Fazer reserva\n[2]Cancelar reserva\n[3]Buscar Reserva\n[4]Listar Reservas\n[5]Editar reserva\n[6]Sair\n')

def main():
    id_ant = 0
    reservas = []
    while True:
        esc = menu()
        if esc == '1':
            nome = input ('Nome do cliente: ')
            numero = input ('Número do quarto: ')
            checkin = input ('Data de entrada: ')
            checkout = input ('Data de saída: ')
            id_ant = (adc_reserva(reservas, id_ant, nome, numero, checkin, checkout))
            
        elif esc == '2':
            id_res = int(input('\nNº da reserva a ser cancelada: '))
            can_reservas(reservas, id_res)

        elif esc == '3':
            nome = input('\nQual nome deseja buscar? ')
            bus_reservas(reservas, nome)

        elif esc == '4':
            print('\nReservas do hotel: \n')
            lis_reservas(reservas)

        elif esc == '5':
            opc = input('\n O QUE VOCÊ DESEJA EDITAR?\n[1]Nome\n[2]Quarto\n[3]Checkin\n[4]Checkout\n')
            edi_reservas(reservas, opc)

        elif esc == '6':
            print('\nENCERRANDO SISTEMA...')
            break

        else:
            print('\nOPÇÃO INVÁLIDA. Escolha outra opção.')

if __name__ == '__main__':
    main()
