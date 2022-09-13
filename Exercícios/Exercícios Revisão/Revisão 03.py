def main():
    A = float(input('Digite o primeiro número: '))
    B = float(input('Digite o segundo número: '))
    C = float(input('Digite o terceiro número: '))
    delta = (B ** 2) - 4 * A * C
    if A == 0:
        print('Impossível calcular')
    elif delta < 0:
        print('Impossível calcular')
    else:
        R1 = (-B + delta ** (1 / 2)) / (2 * A)
        R2 = (-B - delta ** (1 / 2)) / (2 * A)

        print(f'R1 = {R1:.5f}')
        print(f'R2 = {R2:.5f}')

main()