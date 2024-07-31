'''Sistema de hotelaria'''
#adicionar reservas, cancelar reservas, buscar reservas pelo nome do hóspede e listar todas as reservas. 

hotel = {}
reservas = []

def adc_reserva(hotel, nome, numero, checkin, checkout):
    if checkin <= checkin and checkout >= checkout and numero != numero:
        hotel['nome'] = nome
        hotel['numero'] = numero
        hotel['checkin'] = checkin
        hotel['checkout'] = checkout
    else:
        print('\nRESERVA NÃO FEITA.')


def can_reservas():
    pass

def menu():
    return input('\n O QUE DESEJA FAZER?\n[1]Fazer reserva\n[2]Cancelar reserva\n[3]Buscar Reserva\n[4]Listar Reserva\n[5]Sair\n')

def main():
    while True:
        esc = menu()
        if esc == '1':
            nome = input ('Nome do cliente: ')
            numero = input ('Número do quarto: ')
            checkin = input ('Data de entrada: ')
            checkout = input ('Data de saída: ')
            adc_reserva(hotel, nome, numero, checkin, checkout)

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