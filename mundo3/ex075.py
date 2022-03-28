print('='*50)
print(f'{"075 - Análise de dados em uma Tupla":^50}')
print('='*50)

numeros = int(input('1º valor: ')), int(input('2º valor: ')), int(input('3º valor: ')), int(input('4º valor: '))

if 9 in numeros:    
    print(f'O valor 9 apareceu {numeros.count(9)} vezes')
else:
    print('O valor 9 não está presente na tupla.')
if 3 in numeros:
    print(f'O valor 3 apareceu pela primera vez na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não está presente na tupla.')
print('Os números pares digitados foram:', end=' ')
for n in numeros:
    if n % 2 == 0: 
        print(n, end=' ')


