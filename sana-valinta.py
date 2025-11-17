import random

class SanaValinta:
    def valitse_sana(self):
        with open('sanat.txt', 'r') as tiedosto:
            sanat = []
            for rivi in tiedosto:
                rivi = rivi.strip()
                if rivi and not rivi.startswith('#'):
                    sanat.append(rivi.upper())
            return random.choice(sanat)

    def nayta_alaviivat(self, sana):

        return ' '.join('_' for _ in sana)

if __name__ == "__main__":
    sana_valinta = SanaValinta()
    valittu_sana = sana_valinta.valitse_sana()
    print(f"Arvaa sana: ")
    print(sana_valinta.nayta_alaviivat(valittu_sana))
