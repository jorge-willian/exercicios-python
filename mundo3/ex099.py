from time import sleep

def maior(* num):
    print('Analisando os valores passados...')
    
    if len(num) == 0:
        print('Foram passados 0 valores e o maior é 0.')
    
    else:
        for item in num:
            print(item, end=' ')
            sleep(0.5)
        
        print(f'Foram passados {len(num)} valores e o maior é o {max(num)}.')

    print('-' * 50)


print(f'''{"=" * 50}
{"EX099 - Função que descobre o maior"}
{"=" * 50}''')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

