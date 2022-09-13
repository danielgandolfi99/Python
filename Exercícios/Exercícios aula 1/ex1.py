def um(a,b,c):
    return a < b and a < c or c != 0
def dois(a,b,c):
    return a < b  and (a < c or c != 0)
def tres(a,b,c):
    return not (a >= 0 and b == c)
def quatro(a,b,c):
    return not (a >= 0) and not (b == c)
def cinco(a,b,c):
    return (a >= 0 or b == c ) and b > a
def seis(a,b,c):
    return not (a <= b ) or c > b
def sete(a,b,c):
    return not (a <= 0 or c > b)
def oito(a,b,c):
    return a == 0 and b != 0 and c == 0
def nove(a,b,c):
    return a == 0 and b != 0 and c == 0
def dez(a,b,c):
    return a == 0 or b != 0 and c == 0
print(um(10,15,4))
print(dois(10,15,4))
print(tres(1,9,0))
print(quatro(1,9,9))
print(cinco(1,9,0))
print(seis(-2,0,2))
print(sete(-2,0,2))
print(oito(0,1,0))
print(nove(5,0,0))
print(dez(5,0,0))


