print('~'*60)
print(f'{"DESAFIO 064 - LER, SOMAR E CONTAR NÚMEROS INTEIROS":^60}')
print('~'*60)

num = soma = cont = 0

num = int(input('Digite um número (999 para sair): '))
while num != 999:    
    cont += 1
    soma += num
    num = int(input('Digite um número (999 para sair): '))
print(f'Você digitou {cont} números e a soma entre eles é igual a {soma}.')
