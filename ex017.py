# MINHA RESOLUÇÃO
from math import hypot

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjascente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O valor da hipotenusa é igual a {hipotenusa:.2f}.')

# RESOLUÇÃO DO PROFESSOR
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** 0.5
print(f'A hipotenusa vai medir {hi:.2f}')

catop = float(input('Cateto oposto: '))
catad = float(input('Catedo adjacente: '))
hipot = hypot(catop, catad)
print(f'O valor da hipotenbusa é {hipot:.2f}.')