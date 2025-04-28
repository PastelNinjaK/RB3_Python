import math


class Cone:
    def __init__(self,name,rad,height,unit = "meters"):
        """
        Initializes all of the instances
        """
        self.__name = name
        self.__rad = rad
        self.__height = height
        self.__unit = unit
    def __repr__(self):
        """
        returns the properties of the cone.
        """
        return f'''{self.get_name()}'s surface area is equal to {self.print_area()} {self.__unit} squared.
{self.get_name()}'s circumference is equal to {self.print_circumference()} {self.__unit}.
{self.get_name()} is a sphere. It has a volume of {self.print_volume()} cubic {self.__unit}.'''


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
        

    def set_unit(self, units):
        """
        converts the units from meters to a new unit and vice versa
        This one is for the words in __repr__ 
        Arguments:
            units(string): the name of the unit that the user wants to use (default unit is meters) 

        """


        self.__unit = units  # Setter method 
    def get_name(self):
        """
        returns the name of the Cone

        """
        return self.__name

    def print_circumference(self):
        """
        calculates the circumference of the Cone using the formula C = 2πr, where r = the radius of the Cone.

        """
        ans =  2 * math.pi * self.__rad
        ans = round(ans,2)
        return ans
    
    def print_area(self):
        """
        calculates the area of the cone using the formula A = πr((r^2 + h^2)^0.5 + πr),
        where r = the radius of the cone and h = the height of the cone.

        """
        slant = math.sqrt(self.__rad ** 2 + self.__height ** 2)
        ans = math.pi * self.__rad * (self.__rad + slant)
        ans =  round(ans,2)
        return ans

    def print_volume(self):
        """
        
        calculates the volume of a cone using the formula V = (πhr^2)/3,
        where r = the radius of the cone and h = the height of the cone.

        """  
        ans =  (math.pi * (self.__rad ** 2) * self.__height)/3
        ans =  round(ans,2)
        return ans


#Big spaces for my sanity







class Pyramid:
    def __init__(self,name,length,width,height,unit = "meters"):
        self.__name = name
        self.__length = length
        self.__width = width
        self.__height = height
        self.__unit = unit

    def __repr__(self):
        """
        returns the properties of the pyramid.
        """        
        return f'''{self.get_name()}'s area is equal to {self.print_area()} {self.__unit} squared.
{self.get_name()}'s base perimeter is equal to {self.print_perimeter()} {self.__unit}.
{self.get_name()} is a Pyramid. It has a volume of {self.print_volume()} cubic {self.__unit}.'''
    
    def set_factor(self,factor = 1,direction = 0):
        """
        converts the units from meters to a new unit and vice versa.
        This one is for the math used in all of the functions

        Arguments:
            factor(float): the conversion factor from meters to chosen unit(default is meters which is equal to 1).
            direction(int): Optional argument for converting back to meters
        
        """
        if direction != 0:
            self.__length /= factor
            self.__width /= factor
            self.__height /= factor
        else:    
            self.__length *= factor
            self.__width *= factor
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
        returns the name of the Pyramid

        """
        return self.__name


    def print_area(self):
        """
        Returns surface area the base area of Pyramid using the formula A = L*W, where L = the length of Pyramid 
        and W = the width of the Pyramid.
        """
        ans =  self.__length * self.__width
        ans = round(ans,2)
        return ans




    def print_volume(self):
        """
        calculates the volume of the Pyramid using the formula V = LWH/3, where L = length of the base,
        W = width if the base and h = the height of the Pyramid.

        """
        ans  = (self.__height * self.__length * self.__width) / 3
        ans =  round(ans,2)
        return ans  

    def print_perimeter(self):
        """
        returns the perimeter of the base of the Pyramid using the formula
        P = 2(L+W), where L = the length of Pyramid and W = the width of the Pyramid.
        
        """
        
        ans = (self.__length + self.__width) * 2
        ans = round(ans,2)
        return ans      




#Big spaces for my sanity





class Sphere:
    def __init__(self,name,rad,unit = "meters"):
        """
        Initializes all of the instances
        """
        self.__name = name
        self.__rad = rad
        self.__unit = unit 
    def __repr__(self):
        """
        returns the properties of the Sphere.
        """
        return f'''{self.get_name()}'s surface area is equal to {self.print_area()} {self.__unit} squared.
{self.get_name()}'s circumference is equal to {self.print_circumference()} {self.__unit}.
{self.get_name()} is a sphere. It has a volume of {self.print_volume()} cubic {self.__unit}.'''
    
    
    def set_factor(self,factor = 1,direction = 0):
        """
        converts the units from meters to a new unit and vice versa.
        This one is for the math used in all of the functions

        Arguments:
            factor(float): the conversion factor from meters to chosen unit(default is meters which is equal to 1).
            direction(int): Optional argument for converting back to meters
        
        """
        if direction != 0:
            self.__rad /= factor
        else:       
            self.__rad *= factor

        
    def set_unit(self, units):
        self.__unit = units  # Setter method     

    def get_name(self):
        """
        returns the name of the sphere

        """
        return self.__name
    
    def print_area(self):
        """
        calculates the area of the sphere using the formula A = 4πr^2, where r = the radius of the sphere.

        """
        ans = 4 * math.pi * (self.__rad**2)
        ans = round(ans,2)
        return ans
    
    def print_circumference(self):
        """
        calculates the circumference of the sphere using the formula C = 2πr, where r = the radius of the sphere.

        """
        ans =  2 * math.pi * self.__rad
        ans = round(ans,2)
        return ans
    def print_volume(self):
        """
        calculates the volume of the sphere using the formula V = (4/3)πr^3, where r = the radius of the sphere
        and h = the height of the sphere.

        """
        ans = math.pi*(self.__rad**3) * (4/3)
        ans = round(ans,2)
        return ans
    
#Big spaces for my sanity








def sphere_assert():
    meters_to = {"feet":3.28084,
                "inches":39.37008,
                "yards": 1.09361,
                "timbits":23,
                "meters":1  
    }

    # Sphere test
    test_var = Sphere("Big Ball", 1.4)

    assert(test_var.print_area() == 24.63)
    assert(test_var.print_circumference() == 8.8)
    assert(test_var.print_volume() == 11.49) 

    #Unit conversion test (meters to inches)
    test_var.set_factor(meters_to.get('inches'))
    assert(test_var.print_area() == 38176.71)
    assert(test_var.print_circumference() == 346.32)
    assert(test_var.print_volume() == 701409.44) 

    #Unit conversion test (inches to meters)
    test_var.set_factor(meters_to.get('inches'),1)
    assert(test_var.print_area() == 24.63)
    assert(test_var.print_circumference() == 8.8)
    assert(test_var.print_volume() == 11.49) 




def pyramid_assert():
    meters_to = {"feet":3.28084,
                "inches":39.37008,
                "yards": 1.09361,
                "timbits":23,
                "meters":1  
    }
    
    # Pyramid test
    test_var = Pyramid("Pyramid", 10, 5,70)

    assert(test_var.print_area() == 50)
    assert(test_var.print_volume() == 1166.67)
    assert(test_var.print_perimeter() == 30)

    # Unit conversion test (meters to timbits)
    test_var.set_factor(meters_to.get('timbits'))

    assert(test_var.print_area() == 26450)
    assert(test_var.print_volume() == 14194833.33)
    assert(test_var.print_perimeter() == 690)
    
    
    # Unit connversion test (timbits to meters).
    test_var.set_factor(meters_to.get('timbits'),1)
    assert(test_var.print_area() == 50)
    assert(test_var.print_volume() == 1166.67)
    assert(test_var.print_perimeter() == 30)


def cone_assert():
    meters_to = {"feet":3.28084,
                "inches":39.37008,
                "yards": 1.09361,
                "timbits":23,
                "meters":1  
    }    
    
    # Cone test
    test_var = Cone("Sealed funnel",3,2)

    assert(test_var.print_area() == 62.26)
    assert(test_var.print_circumference() == 18.85)
    assert(test_var.print_volume() == 18.85)


    # Unit conversion (meters to yards)
    test_var.set_factor(meters_to.get('yards'))
    
    assert(test_var.print_area() == 74.46)
    assert(test_var.print_circumference() == 20.61)
    assert(test_var.print_volume() == 24.65)

    # Unit conversion (yards to meters)
    test_var.set_factor(meters_to.get('yards'),1)

    assert(test_var.print_area() == 62.26)
    assert(test_var.print_circumference() == 18.85)
    assert(test_var.print_volume() == 18.85)


def test_assert():
    sphere_assert()
    pyramid_assert()
    cone_assert()

def main():
    test_assert()
    
    
if __name__ == "__main__":
    main()