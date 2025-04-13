from math import sqrt

class QuadraticEquation():
    def __init__(self, __a, __b, __c):
        self.__a = __a
        self.__b = __b
        self.__c = __c

    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getDiscriminant(self):
        return ((self.__b**2) - (4*(self.__a * self.__c)))

    def getRoot1(self):

        disc = self.getDiscriminant()
        
        if disc == 0:
            print("This is a linear equation")
            
        if disc < 0:
            return None
        else:
            root1 = (-self.__b + sqrt(disc))/(2*self.__a)
            print(root1)
        
    def getRoot2(self):

        disc = self.getDiscriminant()

        if disc < 0:
            return None
        
        elif disc == 0:
            print("This is a linear equation")
        
        else:
            root2 = (self.__b + sqrt(disc))/(2*self.__a)
            print(root2)

#Enter the values of a,b and c
qe = QuadraticEquation(2,6,7)
qe.getDiscriminant()
qe.getRoot1()
qe.getRoot2()