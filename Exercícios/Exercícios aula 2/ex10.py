def main():
    M = [[11, 12], [6, 10]]
    determinante_primaria = M[0][0] * M[1][1]
    determinante_secundaria = M[0][1] * M[1][0]
    determinante = determinante_primaria - determinante_secundaria
    print(f'A determinante é: {determinante}')

main()