def leiaint(num):
    num = input(num)
    while num.isnumeric() == False:
        print('\033[1;31mErro! Digite um  número inteiro válido\033[m')
        num = input('Digite um número: ')
    return num
    

print(f'''{"=" * 50}
{"EX104 - Validando entrada de dados em Python"}
{"=" * 50}''')

#Programa principal 

n = leiaint('Digite um número: ')
print(f'\033[1;32mVocê acabou de digitar o número {n}!\033[m')