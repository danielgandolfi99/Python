n1 = float(input('Digite o primeiro intervalo: '))
n2 = float(input('Digite o segundo intervalo: '))
x = float(input('Digite o número para verificação: '))
n = float
if ( x >= n1 ) and ( x <= n2 ):
   n = 1
if ( x <= n1 ) and ( x >= n2 ):
    n = 2
while not( n == 1 or n == 2 ):
    print('O número está fora do intervalo')
    x = float(input('Digite o número para verificação: '))
    if (x >= n1) and (x <= n2):
        n = 1
    if (x <= n1) and (x >= n2):
        n = 2
else:
    print('O número está dentro do intervalo.')