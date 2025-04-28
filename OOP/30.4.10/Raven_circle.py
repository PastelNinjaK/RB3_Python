import math
class Circle:
    
    def __init__(self,name,rad,height = 0, unit = 'meters'):
        """
        Initializes all of the instances
        """
        self.__name = name
        self.__unit = unit
        self.__rad = rad 
        self.__height = height 



    def __repr__(self):
        """
        returns the properties of the circle or cylinder
        """
        if self.__height == 0:
            return f'''{self.get_name()}'s Area is equal to {self.print_area()} {self.__unit} squared.
{self.get_name()}'s Circumference is equal to {self.print_circumference()} {self.__unit}
{self.get_name()} is not a cylinder. Volume can not be computed. '''
        else:
            return f'''{self.get_name()}'s Area is equal to {self.print_area()} {self.__unit} squared.
{self.get_name()}'s Circumference is equal to {self.print_circumference()} {self.__unit}.
{self.get_name()} is a cylinder. It has a volume of {self.print_volume()} cubic {self.__unit}.'''

        
    def set_factor(self,factor = 1,direction = 0):
        """
        converts the units from meters to a new unit and vice versa.
        This one is for the math used in all of the functions

        Arguments:
            factor(float): the conversion factor from meters to chosen unit(default is meters which is equal to 1).
            direction(int): Optional argument for converting back to meters
        
        """
        # Setter method 
        if direction != 0:
            self.__rad /= factor
            self.__height /= factor
        else:       
            self.__rad *= factor
            self.__height *= factor 
        
        
    def set_unit(self, units = 'meters'):
        """
        converts the units from meters to a new unit and vice versa
        This one is for the words in __repr__ 
        Arguments:
            units(string): the name of the unit that the user wants to use (default unit is meters) 

        """
        self.__unit = units  # Setter method 

    def get_name(self):
        """
        returns the name of the circle

        """
        return self.__name
    
    def print_area(self):
        """
        calculates the area of the circle using the formula A = πr^2, where r = the radius of the circle.

        """
        ans = math.pi*(self.__rad**2)
        ans = round(ans,2)
        return ans
    
    def print_circumference(self):
        """
        calculates the circumference of the circle using the formula C = 2πr, where r = the radius of the circle.

        """
        ans =  2 * math.pi * self.__rad
        ans = round(ans,2)
        return ans
    def print_volume(self):
        """
        calculates the volume of the cylinder using the formula V = πr^2h, where r = the radius of the circle
        and h = the height of the cylinder.

        """

        ans = math.pi*(self.__rad**2) * self.__height
        ans = round(ans,2)
        return ans

def test_asserts():
    meters_to = {"feet":3.28084,
                "inches":39.37008,
                "yards": 1.09361,
                "timbits":23,
                "meters":1  
    }

    # Flat circle test
    test_var = Circle("test object", 10)
    
    assert(test_var.print_area() == 314.16)
    assert(test_var.print_circumference() == 62.83)
    assert(test_var.print_volume() == 0)


    # Cylinder test
    test_var2 = Circle("test object 2", 36, 9)

    assert(test_var2.print_area() == 4071.5 )
    assert(test_var2.print_circumference() == 226.19)
    assert(test_var2.print_volume() == 36643.54)
    
    # Unit conversion test (meters to timbits)
    test_var2.set_factor(meters_to.get('timbits'))
    assert(test_var2.print_area() == 2153825.66 )#timbits squared
    assert(test_var2.print_circumference() == 5202.48)#timbits
    assert(test_var2.print_volume() == 445841911.17)#timbits cubed


    # Unit conversion test (timbits to meters)

    test_var2.set_factor(meters_to.get('timbits'),1)

    assert(test_var2.print_area() == 4071.5 )
    assert(test_var2.print_circumference() == 226.19)
    assert(test_var2.print_volume() == 36643.54)



def main():
    test_asserts()



if __name__ == "__main__":
    main()