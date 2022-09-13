def main():
    M = [[11, 12, 5], [15, 6, 10], [10, 8, 12]]
    soma = 0
    soma_total = 0
    for linha in range(3):
        for coluna in range(3):
            soma_total += M[linha][coluna]
            if (linha == coluna):
                valor = M[linha][coluna]
                soma += valor
                print(valor)
    print(f'A soma dos valores da diagonal principal é: {soma}')
    print(f'A soma total dos valores é: {soma_total}')
main()