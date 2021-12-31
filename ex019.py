from random import choice
aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
sorteado = choice([aluno1, aluno2, aluno3, aluno4])
print(f'O aluno(a) sorteado foi o(a) {sorteado}!')

# RESOLUÇÃO DO PROFESSOR

n1 = str(input('Primero aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O esclhido foi {escolhido}!')
