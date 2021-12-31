from math import cos, sin, tan, radians
angulo = int(input('Digite um ângulo: '))
print(f'Seno: {sin(radians(angulo)):.2f}\n'
      f'Coseno: {cos(radians(angulo)):.2f}\n'
      f'Tangente: {tan(radians(angulo)):.2f}')