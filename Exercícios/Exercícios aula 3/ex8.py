def main():
    palavra = input('Digite uma palvra: ')
    cont = 0
    for i in palavra:
        if i == 'a' or i == 'A':
            cont = cont + 1
        if i == 'e' or i == 'E':
            cont = cont + 1
        if i == 'i' or i == 'I':
            cont = cont + 1
        if i == 'o' or i == 'O':
            cont = cont + 1
        if i == 'u' or i == 'U':
            cont = cont + 1
    print(f'A quantidade de vogais é: {cont}')

main()