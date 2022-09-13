def main():
    salario = float(input('Informe o salário: '))
    if salario <= 1903.98:
        imposto_de_renda = 0
        valor_imposto = imposto_de_renda * salario
        FGTS = salario * 0.11
        salario_final = salario - valor_imposto
        print(f'Imposto de renda a ser descontado: {valor_imposto}R$ {imposto_de_renda * 100}%')
        print(f'O FGTS a ser depositado é de: {FGTS}R$')
        print(f'O salário final é de: {salario_final}R$')
    if salario >= 1903.99 and salario <= 2826.65:
        imposto_de_renda = 0.075
        valor_imposto = imposto_de_renda * salario
        FGTS = salario * 0.11
        salario_final = salario - valor_imposto
        print(f'Imposto de renda a ser descontado: {valor_imposto}R$ {imposto_de_renda * 100}%')
        print(f'O FGTS a ser depositado é de: {FGTS}R$')
        print(f'O salário final é de: {salario_final}R$')
    if salario >= 2826.66 and salario <= 3751.05:
        imposto_de_renda = 0.15
        valor_imposto = imposto_de_renda * salario
        FGTS = salario * 0.11
        salario_final = salario - valor_imposto
        print(f'Imposto de renda a ser descontado: {valor_imposto}R$ {imposto_de_renda * 100}%')
        print(f'O FGTS a ser depositado é de: {FGTS}R$')
        print(f'O salário final é de: {salario_final}R$')
    if salario >= 3751.06 and salario <= 4664.68:
        imposto_de_renda = 0.225
        valor_imposto = imposto_de_renda * salario
        FGTS = salario * 0.11
        salario_final = salario - valor_imposto
        print(f'Imposto de renda a ser descontado: {valor_imposto}R$ {imposto_de_renda * 100}%')
        print(f'O FGTS a ser depositado é de: {FGTS}R$')
        print(f'O salário final é de: {salario_final}R$')
    if salario > 4664.68:
        imposto_de_renda = 0.275
        valor_imposto = imposto_de_renda * salario
        FGTS = salario * 0.11
        salario_final = salario - valor_imposto
        print(f'Imposto de renda a ser descontado: {valor_imposto}R$ {imposto_de_renda * 100}%')
        print(f'O FGTS a ser depositado é de: {FGTS}R$')
        print(f'O salário final é de: {salario_final}R$')


main()