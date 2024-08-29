class Calculadora:
    def __init__(self):
        pass
    
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
         
    def multiplicar(self, a, b):
        return a * b
         
    def dividir(self, a, b):
        if b == 0:
            print('\nDIVISÃO INVÁLIDA\n')
        return a / b

def main():
    while True:
        calculadora = Calculadora()
        print('\nCALCULADORA\n[1]SOMAR\n[2]SUBTRAIR\n[3]MULTIPLICAÇÃO\n[4]DIVIDIR\n[5]SAIR\n')
        operacao = int(input('DIGITE O QUE DESEJA FAZER: '))
        if operacao == 5:
            print('\nENCERRANDO SISTEMA\n')
            break

        a = float(input('N1: '))
        b = float(input('N2: '))

        if operacao == 1:
            resultado = calculadora.somar(a, b)
        elif operacao == 2:
            resultado = calculadora.subtrair(a, b)
        elif operacao == 3:
            resultado = calculadora.multiplicar(a, b)
        elif operacao == 4:
            resultado = calculadora.dividir(a, b)
        else:
            print('\nOPÇÃO INVÁLIDA\n')
            
        print('O RESULTADO É: ', resultado, '\n')

if __name__ == "__main__":
    main()