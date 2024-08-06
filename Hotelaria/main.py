'''Sistema de hotelaria'''
#adicionar reservas, cancelar reservas, buscar reservas pelo nome do hóspede e listar todas as reservas.

def adc_reserva(reservas, id, nome, numero, checkin, checkout):
        id += 1
        reserva = {
            'id' : id,
            'nome' : nome,
            'numero' : numero,
            'checkin' : checkin,
            'checkout' : checkout
        }
        reservas.append(reserva)
        return id

def can_reservas(reservas, id):
    for reserva in reservas:
        if reserva['id'] == id:
            reservas.remove(reserva)
            print('\nReserva de número {} foi cancelada.\n' .format(id))
            return
    else:
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

def menu():
    return input('\n O QUE DESEJA FAZER?\n[1]Fazer reserva\n[2]Cancelar reserva\n[3]Buscar Reserva\n[4]Listar Reservas\n[5]Editar reserva\n[6]Sair\n')

def main():
    id = 0
    reservas = []
    while True:
        esc = menu()
        if esc == '1':
            nome = input ('Nome do cliente: ')
            numero = input ('Número do quarto: ')
            checkin = input ('Data de entrada: ')
            checkout = input ('Data de saída: ')
            id = (adc_reserva(reservas, id, nome, numero, checkin, checkout))
            print('\nReserva de número {} feita!\n' .format(id))
            
        elif esc == '2':
            id = int(input('\nNº da reserva a ser cancelada: '))
            can_reservas(reservas, id)

        elif esc == '3':
            nome = input('\nQual nome deseja buscar? ')
            bus_reservas(reservas, nome)

        elif esc == '4':
            print('\nReservas do hotel: \n')
            lis_reservas(reservas)

        elif esc == '5':
            pass

        elif esc == '6':
            print('\nENCERRANDO SISTEMA...')
            break

        else:
            print('\nOPÇÃO INVÁLIDA. Escolha outra opção.')

if __name__ == '__main__':
    main()
