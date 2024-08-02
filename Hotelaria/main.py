'''Sistema de hotelaria'''
#adicionar reservas, cancelar reservas, buscar reservas pelo nome do hóspede e listar todas as reservas. 

def adc_reserva(reservas, id, nome, numero, checkin, checkout):
        reserva = {
            'id' : id,
            'nome' : nome,
            'numero' : numero,
            'checkin' : checkin,
            'checkout' : checkout
        }
        reservas.append(reserva)

def can_reservas():
    pass

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
            pass

        elif esc == '3':
            pass

        elif esc == '4':
            pass

        elif esc == '5':
            print('\nENCERRANDO SISTEMA...')
            break

        else:
            print('\nOPÇÃO INVÁLIDA. Escolha outra opção.')

if __name__ == '__main__':
    main()