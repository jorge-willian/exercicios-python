from email import charset
from typing import Counter


print(f'''{"=" * 50}
{"EX083 - VALIDANDO EXPRESSÕES MATEMÁTICAS":^50}
{"=" * 50}''')

expression = []
letters = []
left_parentheses = right_parentheses = 0

expression.append(input(f'Digite a expressão que será analisada: '))

for word in expression:
    for char in word:
        letters.append(char)
        if char == '(':
            left_parentheses += 1
        elif char == ')':
            right_parentheses += 1


if letters[0] == '(' and letters[-1] == ')':   
    if left_parentheses == right_parentheses:
        print('A expressão matemática está correta!')
    else:
        print('A expressão matemática está incorreta!')
else:
    print('A expressão matemática está incorreta!')
         
