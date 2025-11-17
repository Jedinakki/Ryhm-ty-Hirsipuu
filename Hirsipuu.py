from sana_valinta import *
from Sanojen_tarkistin import *
from Hirsipuun_piirto import *

def peli():
    sana = SanaValinta('sanat.txt')
    tarkista = Tarkistin(sana.muunna())
    puu = Piirto()

    laskin = 1

    while True:
        print(puu)
        print(tarkista)

        if laskin == 12:
            print("Hävisit pelin!")
            break

        if sana == tarkista:
            print("Voitit pelin!")
            break

        merkki = input("Anna kirjain: ")

        if tarkista.tarkista(merkki) == False:
            laskin += 1
            puu.seuraava_kuva()


if __name__ == "__main__":
    peli()
        
       


        


