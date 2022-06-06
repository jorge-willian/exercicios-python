print(f'''{"=" * 50}
{"EX089 - NOME E DUAS NOTAS":^50}
{"=" * 50}''')

alunos = []
aluno = []

while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    
    alunos.append(aluno[:])
    aluno.clear()

    opcao = str(input('Deseja continuar? [S/N]: '))

    if opcao in 'Nn':
        break

print('=' * 40)
print(f'{"Nº":<3} {"Nome":<15}{"Média"}')
print('=' * 40)

for id, aluno in enumerate(alunos):
    med = (aluno[1] + aluno[2]) / 2
    print(f'{id:<3} {aluno[0]:<15}{med:.1f}')

while True:
    print('=' * 50)
    id_aluno = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe): '))
    if id_aluno != 999:
        print(f'Notas de {alunos[id_aluno][0]} são {alunos[id_aluno][1:3]}')
    else:
        break

print(f'{" PROGRAMA FINALIZADO ":/^50}')
        

