from abc import ABC , abstractmethod

class Polygon(ABC):
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")

class Rectangle(Polygon):
    def noofsides(self):
        print("I have 4 sides")
r=Triangle()
r.noofsides()
