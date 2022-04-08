print(f'''{'='*50}
{"EX072 - NÚMERO POR EXTENSO":^50}
{'='*50}''')
 
extenso = ('zero','um','dois','tres','quatro',
'cinco','seis','sete','oito','nove','dez','onze',
'doze','treze','quatrorze','quinze','dezesseis',
'dezessete','dezoito','dezenove','vinte')
opcao = 'S'


while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if num in range(0, 21):
            break
        print('O valor digitado não é válido, digite novamente!')    
    print(f'Você digitou o número {extenso[num]}.')
    opcao = str(input('Deseja continuar? S/N ')).upper().strip()
    if opcao == 'N':
        break
print('Programa Finalizado!!')
