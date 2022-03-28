print(f'{ "DESAFIO 067 - TABUADA V3.0 ":=^50}')

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num >= 0:
        print('-' * 50)
        for tab in range(1, 11):
            print(f'{tab:2} X {num} = {tab * num}')
        print('-' * 50)
    else:
        print('Programa tabuada encerrado!')
        break
