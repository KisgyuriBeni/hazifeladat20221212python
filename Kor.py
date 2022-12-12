import math
class Rest01:

    def __init__(self):
        pass

    def korTerulet(self,radius):
        result = math.pow(radius,2)*math.pi
        return result
    def korKerulete(self,radius):
        result = 2*radius*math.pi
        return result

    def haromszogTerulet(self, a, height):
        result = (a*height)/2
        return result
    def haromszogKerulet(self,a,b,c):
        result = a + b + c
        return result

    def hengerTerfogat(self,radius, height):
        result = math.pow(radius,2)*math.pi*height
        return result
    def hengerFelszin01(self,radius, height):
        result = 2 * math.pow(radius,2)*math.pi
        return result
    def hengerFelszin02(self,radius, height):
        result = 2 * radius * math.pi * height
        return result
    
    def gombTerfogat(self,radius):
        result = 4*math.pow(radius,3)*math.pi
        return result
    def gombFelszin(self,radius):
        result = 4 * math.pow(radius,2)*math.pi
        return result
