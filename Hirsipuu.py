from sana_valinta import *
from Sanojen_tarkistin import *
from Hirsipuun_piirto import *

def peli():
    sana = SanaValinta('sanat.txt')
    tarkista = Tarkistin(sana.valitse_sana())
    puu = Piirto()

    laskin = 1

    while True:
        print(puu)
        tarkista.anna_kirjaimet()
        print(tarkista)

        if laskin == 12:
            print("Hävisit pelin!")
            print(f"Oikea sana oli {sana.valittu_sana}")
            break

        if sana.valittu_sana == tarkista.paljastus:
            print("Voitit pelin!")
            break



        merkki = input("Anna kirjain: ")

        if tarkista.tarkista(merkki) == False:
            laskin += 1
            puu.seuraava_kuva()

        



if __name__ == "__main__":
    peli()
        
       


        



