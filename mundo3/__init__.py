from dataclasses import replace


def leiadinheiro(valor):
    valor_valido = False
    while not valor_valido:
        entrada = str(input(valor)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[1;31mERRO! O valor {entrada} é inválido! Digite novamente!\033[m')
        else:
            valor_valido = True
            return float(entrada)