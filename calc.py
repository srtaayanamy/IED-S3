class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self):
        resultado = self.num1 + self.num2
        print ('\nA SOMA É: ', resultado)

    def subtrair(self):
        resultado = self.num1 - self.num2
        return resultado

    def multiplicar(self):
        resultado = self.num1 * self.num2
        return resultado

    def dividir(self):
        resultado = self.num1 / self.num2
        return resultado

def menu():
        print('\nCALCULADORA\n[1]SOMAR\n[2]SUBTRAIR\n[3]MULTIPLICAÇÃO\n[4]DIVIDIR\n[5]SAIR\n')


def numeros():
    num1 = input('N1: ')
    num2 = input('N2: ')
    return num1, num2

def main():
    calc = Calculadora(num1, num2)
    while True:
        menu()
        esc = input(' ')
        if esc == '1':
            num1 = int(input('N=\n'))
            print('+')
            num2 = int(input('N=\n'))
            print('=')
            calc.somar(num1, num2)

        else:
            print('\nOPÇÃO INVÁLIDA\n')

if __name__ == '__main__':
    main()
