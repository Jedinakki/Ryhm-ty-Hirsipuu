class Tarkistin:
    def __init__(self,sana:str):
        self.sana = sana
        self.paljastus = "_"*len(sana)
        self.kaytetyt_merkit = []
    
    def tarkista(self,merkki):
        if merkki in self.kaytetyt_merkit:
            raise ValueError("merkki on jo listalla")
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
                
    def __str__(self):
        return self.paljastus
