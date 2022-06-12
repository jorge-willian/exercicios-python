from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
        
    if inicio < fim:        
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        for cont in range(inicio, fim + 1, passo):
            print(cont, end=' ')
            sleep(0.5)
        print('FIM!')

    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        for cont in range(inicio, fim - 1, -passo):
            print(cont, end=' ')
            sleep(0.5)
        print('FIM!')
    
    print('-' * 50)


print(f'''{"-" * 50}
{"EX098 - Função de Contador":^50}
{"-" * 50}''')

contador(1, 10, 1)
contador(10, 0, 2)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)



