extenso = ('um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatrorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte').upper
while True:
    num = int(input('Digite um número entre 1 e 20: '))
    if num == 0:
        break
    while num not in range(1, 21):
        print('O valor digitado não é válido, digite novamente!')
        num = int(input('Digite um número entre 1 e 20: '))    
    print(f'Você digitou o número {extenso[num - 1]}',)
print('Programa Finalizado!!')