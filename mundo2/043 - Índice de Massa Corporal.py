print(f'{" CALCULADORA IMC ":-^50}')

    
peso = float(input('Digite o peso: (Kg) '))
alt = float(input('Digite a altura: (m) '))
imc = peso / (alt ** 2)

if imc < 18.5:
    print(f'Seu IMC é igual a {imc:.1f} e está classificado como ABAIXO DO PESO.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é igual a {imc:.1f} e está classificado como PESO IDEAL.')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é igual a {imc:.1f} e está classificado como SOBREPESO.')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é igual a {imc:.1f} e está classificado como OBESIDADE.')
else:
    print(f'Seu IMC é igual a {imc:.1f} e está classificado como OBESIDADE MÓRBIDA.')

