print(f'''{"="*50}
{"077 - CONTANDO VOGAIS EM UMA TUPLA":^50}
{"="*50}''')

palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO',
'GRÁTIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR',
'FUTURO')

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiouáàâãéêíóôõú':
            print(letra, end=' ')

