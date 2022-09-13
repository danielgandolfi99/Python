salario = float(input('Digite o salario: '))
qnt_horas = float(input('Digite a quantidade de horas trabalhadas no mes: '))
qnt_horas_extras = float(input('Digite a quantidade de horas extras no mes: '))
valor_hora = salario / qnt_horas
valor_hora_extra = qnt_horas_extras * valor_hora * 2
valor_final = valor_hora_extra + salario
print('O valor a ser recebido nesse mês será de: ',valor_final)