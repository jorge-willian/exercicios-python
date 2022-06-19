def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (KeyboardInterrupt):
            print('\033[1;31mErro! O usuário não digiou nenhum valor!\033[m')
        except:
            print('\033[1;31mErro! Digite um número inteiro válido!\033[m')
        else:
            return n

def leiafloat(num):
    while True:
        try:
            n = float(input(num))        
        except (KeyboardInterrupt):
            print('\033[1;31mErro! Usuário não digitou nenhum valor.\033[m')
        except:
            print('\033[1;31mErro! Digite um número real válido!\033[m')
        else:
            return n

print(f'''{"=" * 50}
{"EX113 - Funções aprofundadas em Python".center(50)}
{"=" * 50}''')


inteiro = leiaint('Digite um valor inteiro: ')
real = leiafloat('Digite um valor real: ')

print(f'Você digitou o número inteiro {inteiro} e o real {real}.')
    