print(f'{" DESAFIO 053 - PALÍNDROMO ":/^50}')

frase = str(input('Digite a frase: ')).upper().replace(' ','')
fraseinvertida = frase[::-1]

if frase == fraseinvertida:
    print(f'''A frase é um palíndromo
O inverso da frase {frase} é {fraseinvertida}''')
else:
    print(f'''A frase {frase} não é um palíndromo
O inverso da frase {frase} é {fraseinvertida}''')
