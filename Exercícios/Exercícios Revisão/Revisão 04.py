def main():
    vert_invert = input("Informe se o animal é vertebrado ou invertebrado: ")
    if vert_invert == "vertebrado":
        vertebrado()
    if vert_invert == "invertebrado":
        invertebrado()
    if vert_invert != "vertebrado" and vert_invert != "invertebrado":
        print("Animal digitado errado.")

def vertebrado():
    ave_mamifero = input("Informe se o animal é uma ave ou mamifero: ")
    if ave_mamifero == "ave":
        ave()
    if ave_mamifero == "mamifero":
        mamifero()
    if ave_mamifero != "ave" and ave_mamifero != "mamifero":
        print("Animal digitado errado.")

def ave():
    global animal
    carni_oni = input("Informe se o animal é carnivoro ou onivoro: ")
    if carni_oni == "carnivoro":
        animal = "aguia"
        print(f"O animal correspondente é: {animal}")
    if carni_oni == "onivoro":
        animal = "pomba"
        print(f"O animal correspondente é: {animal}")
    if carni_oni != "carnivoro" and carni_oni != "onivoro":
        print("Animal digitado errado.")

def mamifero():
    global animal
    oni_herb = input("Informe se o animal é onivoro ou herbivoro: ")
    if oni_herb == "onivoro":
        animal = "homem"
        print(f"O animal correspondente é: {animal}")
    if oni_herb == "herbivoro":
        animal = "vaca"
        print(f"O animal correspondente é: {animal}")
    if oni_herb != "onivoro" and oni_herb != "herbivoro":
        print("Animal digitado errado.")

def invertebrado():
    inseto_anelideo = input("Informe se o animal é inseto ou anelideo: ")
    if inseto_anelideo == "inseto":
        inseto()
    if inseto_anelideo == "anelideo":
        anelideo()
    if inseto_anelideo != "inseto" and inseto_anelideo != "anelideo":
        print("Animal digitado errado.")

def inseto():
    global animal
    hema_herb = input("Informe se o animal é hematofago ou herbivoro: ")
    if hema_herb == "hematofago":
        animal = "pulga"
        print(f"O animal correspondente é: {animal}")
    if hema_herb == "herbivoro":
        animal = "lagarta"
        print(f"O animal correspondente é: {animal}")
    if hema_herb != "hematofago" and hema_herb != "herbivoro":
        print("Animal digitado errado.")

def anelideo():
    global animal
    hema_oni = input("Informe se o animal é hematofago ou onivoro: ")
    if hema_oni == "hematofago":
        animal = "sanguessuga"
        print(f"O animal correspondente é: {animal}")
    if hema_oni == "onivoro":
        animal = "minhoca"
        print(f"O animal correspondente é: {animal}")
    if hema_oni != "hematofago" and hema_oni != "onivoro":
        print("Animal digitado errado.")

main()