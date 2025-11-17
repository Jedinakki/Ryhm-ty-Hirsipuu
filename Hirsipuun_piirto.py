class Piirto:
    def __init__(self):
        self.__hirsipuu = ["       ","       ","       ","       ","       ","       "]
        self.__vaihe = 0
    def seuraava_kuva(self):
        self.__vaihe +=1
        if self.__vaihe == 1:
            self.__hirsipuu[5]="_______"
        if self.__vaihe == 2:
            self.__hirsipuu[1]="      |"
            self.__hirsipuu[2]="      |"
            self.__hirsipuu[3]="      |"
            self.__hirsipuu[4]="      |"
            self.__hirsipuu[5]="______|"
        if self.__vaihe == 3:
            self.__hirsipuu[5]="_____/|"
        if self.__vaihe == 4:
            self.__hirsipuu[0]="   ____"
        if self.__vaihe == 5:
            self.__hirsipuu[1]="   |  |"
        if self.__vaihe == 6:
            self.__hirsipuu[2]="   O  |"
        if self.__vaihe == 7:
            self.__hirsipuu[3]="   |  |"
        if self.__vaihe == 8:
            self.__hirsipuu[3]="   |- |"
        if self.__vaihe == 9:
            self.__hirsipuu[3]="  -|- |"
        if self.__vaihe == 10:
            self.__hirsipuu[4]="    \ |"
        if self.__vaihe == 11:
            self.__hirsipuu[4]="   /\ |"
        

    def __str__(self):
        return f"{self.__hirsipuu[0]}\n{self.__hirsipuu[1]}\n{self.__hirsipuu[2]}\n{self.__hirsipuu[3]}\n{self.__hirsipuu[4]}\n{self.__hirsipuu[5]}\n"
        