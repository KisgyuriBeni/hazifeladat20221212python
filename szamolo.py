from Kor import Rest01
from inputData import Rest02

class calc:
    def __init__(self):

        self.radius = 0
        self.height = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.choosen = 0
        self.rest01 = 0
        self.rest02 = 0
        self.rest03 = 0
        self.data = 0

    #def getData(self):
       # self.radius = float(input("Sugár:"))
       # self.height =float(input("Magasság:"))
       # self.a =float(input("a értéke:"))
       # self.b =float(input("b értéke:"))
       # self.c =float(input("c értéke:"))

    def getResult01(self):
        self.rest01 = Rest01().korTerulet(self.radius)
        print("Kör Területe:{:.3f} Négyzetméter".format(self.rest01))
    def getResult02(self):
        self.rest02 = Rest01().korKerulet(self.radius)
        print("Kör Kerülete:{:.3f} Négyzetméter".format(self.rest02))


    def choosenResult(self):
        print("Kör Területe[1] Kör Kerülete[2] HáromszögTerülete[3] HáromszögKerülete[4] HengerTérfogata[5] HengerFelszíne[6] GömbTérfogata[7] GömbFelszíne[8]")
        self.choosenResult = int(input("Válassz:"))
        
        if self.choosen == 1:
            self.data = Rest02().getKorData(self.radius)
            Calc.getResult01()
        elif self.choosen == 2:
            self.data = Rest02().getKorData(self.radius)
            Calc.getResult02()
        else:
            print("Hibás adat!")


Calc = calc()
Calc.choosenResult()
