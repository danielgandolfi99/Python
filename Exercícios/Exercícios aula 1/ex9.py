num = int(input('Digite um número entre 10000 e 30000: '))
if num < 10000 or num > 30000:
    print('Número Inválido.')
else:
    num = str(num)
    digito1 = int(num[0])*2
    digito2 = int(num[1])*3
    digito3 = int(num[2])*4
    digito4 = int(num[3])*5
    digito5 = int(num[4])*6
    soma = digito1 + digito2 + digito3 + digito4 + digito5
    resto = soma % 7
    print('A soma de todos os é: ',soma)
    print('O resto da soma é: ', resto)