class Tarkistin:
    def __init__(self,sana:str):
        self.sana = sana
        self.paljastus = "_"*len(sana)
        self.kaytetyt_merkit = []
    
    def tarkista(self,merkki:str):
        merkki=merkki.upper()
        if merkki in self.kaytetyt_merkit:
            print("merkki on jo listalla")
            return
        if merkki in self.sana:
            self.paljasta(merkki)
            self.kaytetyt_merkit.append(merkki)
            return True
        else:
            self.kaytetyt_merkit.append(merkki)
            return False
    
    def paljasta(self,merkki):
        paikka = 0
        for kohta in self.sana:
            if kohta == merkki:
                lista = list(self.paljastus)
                lista[paikka]=merkki
                self.paljastus = "".join(lista)
            paikka +=1

    def anna_kirjaimet(self):
        print(", ".join(self.kaytetyt_merkit))
    def __str__(self):
        return self.paljastus
