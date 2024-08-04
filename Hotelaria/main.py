'''Sistema de hotelaria'''
#adicionar reservas, cancelar reservas, buscar reservas pelo nome do hóspede e listar todas as reservas. 

#vou ter que limitar o numero de quartos se n, n vou conseguir criar uma lógica pra n permitir reservas repetidas

def adc_reserva(reservas, id, nome, numero, checkin, checkout):
        reserva = {
            'id' : id,
            'nome' : nome,
            'numero' : numero,
            'checkin' : checkin,
            'checkout' : checkout
        }
        reservas.append(reserva)

def can_reservas(reservas, nome):
    for reserva in reservas:
        if reserva['nome'] == nome:
            reservas.remove(reserva)
            print('\nReserva no nome de {} foi cancelada.\n' .format(nome))
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

def menu():
    return input('\n O QUE DESEJA FAZER?\n[1]Fazer reserva\n[2]Cancelar reserva\n[3]Buscar Reserva\n[4]Listar Reserva\n[5]Sair\n')

def main():
    reservas = []
    while True:
        esc = menu()
        if esc == '1':
            id = input ('Id da reserva: ')
            nome = input ('Nome do cliente: ')
            numero = input ('Número do quarto: ')
            checkin = input ('Data de entrada: ')
            checkout = input ('Data de saída: ')
            adc_reserva(reservas, id, nome, numero, checkin, checkout)
            print('\nReserva feita!\n')
            
        elif esc == '2':
            nome = input ('\nNome do cliente a ser cancelado: ')
            can_reservas(reservas, nome)

        elif esc == '3':
            nome = input('\nQual nome deseja buscar? ')
            bus_reservas(reservas, nome)

        elif esc == '4':
            pass

        elif esc == '5':
            print('\nENCERRANDO SISTEMA...')
            break

        else:
            print('\nOPÇÃO INVÁLIDA. Escolha outra opção.')

if __name__ == '__main__':
    main()
