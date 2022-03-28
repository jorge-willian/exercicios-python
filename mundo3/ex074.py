from random import sample

num = tuple(sample(range(0, 10), 5))
print('Os números sorteados foram: ', end='')
for c in num: #PARA CADA ITEM EM NUM
    print(c, end=' ')

print(f'''\nO maior número sorteado foi {max(num)}
O menor número sorteado foi {min(num)}''')