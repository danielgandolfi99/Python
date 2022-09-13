def main ():
    par = list()
    impar = list()
    num = [10, 2, 32, 14, 35, 46, 17, 58, 199, 19]
    for n in num:
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)

    print(f'Todos os pares: {par}')
    print(f'Todos os impares: {impar}')
    print(num[2:4])
    print(num[1::3])

main()

