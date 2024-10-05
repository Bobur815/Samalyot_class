

class Samolyot:

    model = "Boeing 787 Dreamliner"
    ishlab_chiqaruvchi = "Boeing Inc."
    yil = 2011
    sigimi = 300
    max_tezlik = 802

    def __init__(self):
        self.balandlik = 0
        self.tezlik = 0

    def __ge__ (self):
        return self.tezlik>=250
    
    def __eq__(self):
        return self.tezlik<=0
    
    def uchish(self):
        if self.balandlik==0:
            self.balandlik = 10000
            print(f"{self.model} {self.tezlik} km/soat tezlikda havoga ko'tarildi va {self.balandlik} metr balandlikda uchmoqda")
        else:
            print(f"{self.model} allaqachon havoda")

    def qonish (self):
        self.balandlik = 0
        self.tezlik = 0
        print(f"{self.model} muvaffaqiyatli qo'ndi")

    def tezlashish(self,tezla):
        self.tezlik+=tezla
        print(f"{self.model}ning tezligi {self.tezlik} km/soatga yetdi")

    def sekinlashish(self,sekinla):
        if self.tezlik-sekinla>=0:
            self.tezlik-=sekinla
            print(f"{self.model}ning tezligi {self.tezlik} km/soatga sekinladi")
        else:
            self.tezlik = 0
            print(f"{self.model}ning tezligi {self.tezlik} tushdi")


    def haqida(self):
        print(f"Modeli:\t\t{self.model}\nIshlab chiq.:   {self.ishlab_chiqaruvchi}\nYil:\t\t{self.yil}\nSig'imi:\t{self.sigimi}\nYuqori texlik:\t{self.max_tezlik}")

if __name__=="__main__":

    samalyot = Samolyot()
    print("\nSamalyotimiz haqida qisqacha ma'lumot:\n")
    samalyot.haqida()
    n = int(input("\nSamalyot 250 tezlikda havoga ko'tariladi\nOz-ozdan tezlik qo'shin:\n"))

    if n<=800:
        while 1:
            samalyot.tezlashish(n)
            if samalyot.__ge__():
                samalyot.uchish()
                break
            else:
                n = int(input("Havoga ko'tarilish uchun yana tezlik qo'shin:\n"))
    else:
        raise Exception("Eng yuqori tezlikdan o'tib ketdi!")
    
    n = int(input("\nEndi samalyotni qo'ndiramiz\nOz-ozdan tezlikni kamaytirin:\n"))
    if n<=samalyot.tezlik:
        while 1:
            samalyot.sekinlashish(n)
            if samalyot.__eq__():
                samalyot.qonish()
                break
            else:
                n = int(input("Qo'nish uchun yana tezlikni kamaytirin:\n"))
    else:
        raise Exception("Noto'g'ri tezlik kiritdingiz!")




