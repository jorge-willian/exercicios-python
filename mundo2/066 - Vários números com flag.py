print(f'{" DESAFIO 066 - VÁRIOS NÚMEROS COM FLAG ":=^50}')

soma = cont = 0

while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
    
print(f'A soma dos {cont} valores foi de {soma}')
