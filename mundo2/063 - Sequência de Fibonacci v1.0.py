print(f'{" DESAFIO 063 - SEQUENCIA DE FIBONACCI V1.0 ":/^50}')
termos = int(input('Quantos termos quer mostrar? '))
cont = 3
t1 = 0
t2 = 1
print('='*50)
print(f'{t1} → {t2}', end='')
while cont < termos:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
print('='*50)
 
