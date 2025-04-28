class Rectangle:
    def __init__(self,name,length,width,height = 0, unit = 'meters'):
        """
        Initializes all of the instances
        """
        self.__name = name
        self.__length = length
        self.__width = width
        self.__height = height
        self.__unit = unit



    def __repr__(self):
        """
        returns the properties of the rectangle or rectangular prism
        """        
        if self.__height == 0:
            return f'''{self.get_name()}'s Area is equal to {self.print_area()} {self.__unit} squared.
{self.get_name()}'s Perimeter is equal to {self.print_perimeter()} {self.__unit}.
{self.get_name()} is not a rectangular prism. Volume can not be computed.'''
        else:
            return f'''{self.get_name()}'s Area is equal to {self.print_area()}
{self.get_name()}'s Perimeter is equal to {self.print_perimeter()} {self.__unit}.
{self.get_name()} is a rectangular prism. It has a volume of {self.print_volume()} cubic {self.__unit}.'''

    def set_factor(self,factor = 1,direction = 0):
        """
        converts the units from meters to a new unit and vice versa.
        This one is for the math used in all of the functions

        Arguments:
            factor(float): the conversion factor from meters to chosen unit (default is meters which is equal to 1)
            direction(int): Optional argument for converting back to meters
        
        """ 
        # Setter method        

        if direction != 0:
            self.__length /= factor
            self.__width /= factor
            self.__height /= factor
        else:    
            self.__length *= factor
            self.__width *= factor
            self.__height *= factor
        
    def set_unit(self, units):
        self.__unit = units  # Setter method     

    def get_name(self):
        """
        Returns the name of the rectangle.
        """
        return self.__name
    def print_area(self):
        """
        Returns surface area the area of rectangle using the formula A = L*W, where L = the length of rectangle 
        and W = the width of the rectangle.
        """


        ans =  self.__length * self.__width
        ans = round(ans,2)
        return ans
    def print_volume(self):
        """
        returns the volume of the rectangular prism using the formula V =  L*W*H,
        where L = the length of rectangular prism, W = the width of the rectangular prism,
        and H = the height of the rectangular prism.

        
        """


        ans =  self.__length * self.__height * self.__width
        ans = round(ans,2)
        return ans
    def print_perimeter(self):
        """
        returns the perimeter of the rectangle/rectangular prism using the formula
        P = 2(L+W), where L = the length of rectangle and W = the width of the rectangle.
        
        """

        ans = (self.__length + self.__width) * 2
        ans = round(ans,2)
        return ans
    

def test_assert():
    meters_to = {"feet":3.28084,
                "inches":39.37008,
                "yards": 1.09361,
                "timbits":23,
                "meters":1  
    }
    # Rectangle test
    test_var = Rectangle("test obj", 10,40)

    assert(test_var.print_area() == 400)
    assert(test_var.print_volume() == 0)
    assert(test_var.print_perimeter() == 100)

    # Rectangular prism test
    test_var2 = Rectangle("Prism test", 40,60,10)
    assert(test_var2.print_area() == 2400)
    assert(test_var2.print_perimeter() == 200)
    assert(test_var2.print_volume() == 24000)
    
    # Unit conversion test (meters to feet)
    test_var2.set_factor(meters_to.get('feet'))
    assert(test_var2.print_area() == 25833.39)# feet squared
    assert(test_var2.print_perimeter() == 656.17)# feet
    assert(test_var2.print_volume() == 847552.08)# feet cubed

    # Unit conversion test (feet to meters)
    test_var2.set_factor(meters_to.get('feet'),1)
    assert(test_var2.print_area() == 2400)
    assert(test_var2.print_perimeter() == 200)
    assert(test_var2.print_volume() == 24000)



def main():
    test_assert()


if __name__ == "__main__":
    main()