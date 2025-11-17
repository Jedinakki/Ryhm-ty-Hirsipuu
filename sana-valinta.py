import random

def valitse_sana():

    with open('sanat.txt', 'r') as tiedosto:
        sanat = []
        for rivi in tiedosto:
            rivi = rivi.strip()
            if rivi and not rivi.startswith('#'):
                sanat.append(rivi.upper())
        
        return random.choice(sanat)

def nayta_alaviivat(sana):
    """Näyttää sanan alaviivoineen _ _ _"""
    return ' '.join('_' for _ in sana)

if __name__ == "__main__":
    valittu_sana = valitse_sana()
    print(f"Arvaa sana: ")
    print(nayta_alaviivat(valittu_sana))
