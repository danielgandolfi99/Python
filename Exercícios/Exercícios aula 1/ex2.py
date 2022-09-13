import math

r = float(input('Digite o valor do raio: '))

def diam():
    diam = 2 * r
    return diam

def circ():
    circ = 2 * math.pi * r
    return circ

def area():
    area_s = (4 * math.pi * r)**2
    return area_s
def volume():
    volume = (4/3) * math.pi * r ** 3
    return volume

def main():
    print('O diêmetro é {} : '.format(diam()))
    print('A circunferência é {} : '.format(circ()))
    print('A área da superficie é {} : '.format(area()))
    print('O volume é {} : '.format(volume()))

main()
