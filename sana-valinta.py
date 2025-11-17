import random

class SanaValinta:
    def __init__(self, tiedostonimi='sanat.txt'):
        self.tiedostonimi = tiedostonimi
        self.sanat = self.lataa_sanat()

    def lataa_sanat(self):
        sanat = []
        with open(self.tiedostonimi, 'r') as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.strip()
                if rivi and not rivi.startswith('#'):
                    sanat.append(rivi.upper())
        return sanat

    def valitse_sana(self):
        return random.choice(self.sanat)

    def nayta_alaviivat(self, sana):
        return ' '.join('_' for _ in sana)

if __name__ == "__main__":
    sana_valinta = SanaValinta()
    valittu_sana = sana_valinta.valitse_sana()
    print(f"Arvaa sana: ")
    print(sana_valinta.nayta_alaviivat(valittu_sana))
