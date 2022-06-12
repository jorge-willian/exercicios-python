def titulo(texto):
    print('=' * 50)
    print(f'{texto:^50}')
    print('=' * 50)

def area(larg, comp):
    area_total = larg * comp
    print(f'A área total do terreno {larg} x {comp} é de {area_total:.2f} m²')


titulo('EX096 - Função que calcula área')

l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))

area(l, c)
