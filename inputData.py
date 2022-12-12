class Rest02:

    def __init__(self):
        self.radius = 0
        self.height = 0
        self.a = 0
        self.b = 0
        self.c = 0
    def getKorData(self):
        self.radius = float(input("Sugár:"))
    def getHaromszogData(self):
        self.a = float(input("'a' értéke:"))
        self.b = float(input("'b' értéke:"))
        self.c = float(input("'c' értéke:"))
    def getHengerData(self):
        self.radius = float(input("Sugár:"))
        self.height = float(input("Magasság:"))