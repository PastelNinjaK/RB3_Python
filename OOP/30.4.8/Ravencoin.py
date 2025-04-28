import math
pi = math.pi
class Coin:
    def __init__(self,coin_name,rad,material,in_cents):
        """
        Initializes all of the instances
        """
        self.coin_name = coin_name
        self.rad = rad
        self.material = material
        self.in_cents = in_cents
        


    def __repr__(self):
        return f'''\nA {self.coin_name} is made out of {self.material} and has a value of {self.in_cents} cents.
The surface area of one side of a {self.coin_name} is {self.get_area()}mm^2.
A {self.coin_name} has a circumference of {self.coin_circumference()}mm.'''
    
    def coin_circumference(self):
        """
        calculates the circumference of a coin using the formula C = 2πr, where r = the radius of the coin.

        Example:
            rad = 12.7
            coin_circumference()
            79.79645340118074

        
        """
        ans = 2 * pi * self.rad
        return ans
    
    def get_area(self):
        """
        calculates the area of a coin using the formula A = πr^2, where r = the radius of the coin.

        Example:
            rad = 12.7
            get_area()
            506.7074790974977
        
        """
        ans = pi*(self.rad**2)
        return ans


def test_assert():
    """
    checks if the instance method inside Coin class works

    """
    test_var1 =  Coin("Nickel",10.6,"Nickel-plated steel",5)
    assert(test_var1.get_area() == 352.98935055734916)
    assert(test_var1.coin_circumference() == 66.6017642561036)
    test_var2 = Coin("Quarter",13.5,"Nickel-plated steel",25)
    assert(test_var2.get_area() == 572.5552611167398)  
    assert(test_var2.coin_circumference() == 84.82300164692441)

def main():
    test_assert()



if __name__ == "__main__":
    main()

