import math



class Mathings:
    @staticmethod

    def add(x,y):
        """
        takes 2 numbers and returns their sum.
        Arguments:
            x(int/float): the first number
            y(int/float): the second number
        Example:
            print(Mathings.add(1,4))
            >>> 1 + 4 = 5
        """
        # not needed since the main loop has a way of dealing with non number inputs
        # only here for asserts
        if type(x) == str or type(y) == str:
            return("Invalid input")
        try:
            ans = x+y
            return f"{x} + {y} = {ans}"
        except TypeError:
            return "Invalid input"
        except OverflowError:
            return "One or both of your inputs are way too big."
    
    @staticmethod

    def subtract(x,y):
        """
        takes 2 numbers and returns their difference.
        Arguments:
            x(int/float): the first number
            y(int/float): the second number
        Example:
            print(Mathings.subtract(1,4))
            >>> 1 - 4 = -3
        """
        # not needed since the main loop has a way of dealing with non number inputs
        # only here for asserts
        if type(x) == str or type(y) == str:
            return("Invalid input")
        try:
            ans = x - y
            return f"{x} - {y} = {ans}"
        except TypeError:
            return "Invalid input"   
        except OverflowError:
            return "One or both of your inputs are way too big." 
    
    @staticmethod
    def multiplication(x,y):
        """
        takes 2 numbers and returns their product.
        Arguments:
            x(int/float): the first number
            y(int/float): the second number
        Example:
            print(Mathings.multiplication(4,-5))
            >>> 4 * -5 = -20
        """
        # not needed since the main loop has a way of dealing with non number inputs
        # only here for asserts        
        if type(x) == str or type(y) == str:
            return("Invalid input")
        try:
            ans = x * y
            return f"{x} * {y} = {ans}"
        except TypeError:
            return "Invalid input"
        except OverflowError:
            return "One or both of your inputs are way too big."    

    @staticmethod    
    def divide(x,y):
        """
        takes 2 numbers and returns their product.
        Arguments:
            x(int/float): the first number
            y(int/float): the second number
        Example:
            print(Mathings.divide(81,9))
            >>> 81 / 9 = 9
        """
        # not needed since the main loop has a way of dealing with non number inputs
        # only here for asserts
        if type(x) == str or type(y) == str:
            return("Invalid input")
        try:
            ans =  x/y
            return f"{x} / {y} = {ans}"
        except TypeError:
            return "Invalid input" 
        except ZeroDivisionError:
            return "infinity"
        except OverflowError:
            return "One or both of your inputs are way too big."
               
    @staticmethod
    def pythagoras(a,b):
        """
        Takes 2 numbers and uses the pythagorean theorem to find the third number.
        Arguments:
            a(int/float): the first number
            b(int/float): the second number
        Example:
            print(Mathings.pythagoras(12,5))
            >>> c = 13    
        """
        # not needed since the main loop has a way of dealing with non number inputs
        # only here for asserts        
        if type(a) == str or type(b) == str:
            return("Invalid input")
        try:
            c_squared = a ** 2 + b ** 2
            c = c_squared ** 0.5
            return f"c = {c}"
        except TypeError:
                return "Invalid input" 
        except OverflowError:
            return "One or both of your inputs are way too big."     
    
    @staticmethod
    def power(base,exponent):
        """
        Takes one number and raises it to the power of another.
        Arguments:
            base(int/float): the first number
            exponent(int/float): the second number
        Example:
            print(Mathings.power(2,2))
            >>> 2 ^ 2 = 4 
        
        
        """
        # not needed since the main loop has a way of dealing with non number inputs
        # only here for asserts
        if type(base) == str or type(exponent) == str:
            return("Invalid input")
        try:
            ans = base ** exponent
            return f"{base} ^ {exponent} = {ans}"
        except TypeError:
            return "Invalid input" 
        except OverflowError:
            return "One or both of your inputs are way too big."  
    

    @staticmethod
    def getKthDigit(n,k):
        """
        finds the kth digit of a number

        Arguments:
            n(int): the reference number
            k(int): the position of the digit that the user wants to locate
        Example:
            print(Mathings.getKthDigit(1223526,0))
            >>> the 0th digit of 1223526 is 6


        """
        # not needed since the main loop has a way of dealing with non number inputs
        # only here for asserts       
        if type(n) == str or type(k) == str:
            return("Invalid input")    
        try:
            number = abs(n) # turns n to a positive number
            k = int(k)
            if k < 0:
                return f"{n} can't have a negative kth digit."                
            number = abs(n) 
            digit =  10 ** k # assigns digit to be equal to 10^k
            rest = (number // digit ) # divides the value of number and digit and drops the remainder
            answer = rest % 10 # gets the gets the ones place of rest
            return f"the {k}th digit of {n} is {int(answer)}"
        except TypeError:
            return "Invalid input" 
        except OverflowError:
            return "One or both of your inputs are way too big."  
    @staticmethod    
    def short1():
        """
        Exaplains what static method is and why we use it
        
        """
        text = '''Static method is a method that belongs to a class but does not interact with any other instances of said class.
It’s used when a coder wants to group related functions together for better organization.
Static methods are useful when you need to perform a task that logically fits within the class but operates independently, meaning the method does not rely on instance variables or other instance methods..'''
        return text
    @staticmethod
    def short2():
        """
        Explains the purpose of the @staticmethod decorator
        """
        text = '''@staticmethod tells Python that the class should be treated as a static method
It allows to define as function inside a class without creating a new instance.
'''
        return text 
    @staticmethod 
    def short3():
        """
        Explains the difference between a static method and an instance method
        """

        text = '''A static method does not have self or cls as parameters. It also cannot access or modify class or instance data.
An instance method has self as the first parameter, which allows it to access and modify instance data.
'''
        return text      




def test_assert():
    """
    test every function in Mathings Class

    Example:
        assert(Mathings.add(2,3) == "2 + 3 = 5")
        >>> (Nothing cause it passed the assert test)

    
    """
    assert(Mathings.add(2,3) == "2 + 3 = 5")
    assert(Mathings.add("hjgflhagd",5 == "Invalid input"))
    assert(Mathings.subtract(2.0,5.0) == "2.0 - 5.0 = -3.0")
    assert(Mathings.subtract(56,"gafklhgalfgeiyg") == "Invalid input" )
    assert(Mathings.multiplication(5,2) == "5 * 2 = 10")
    assert(Mathings.multiplication("jkgsafkgk",10) == "Invalid input")
    assert(Mathings.divide(72,8.0) == "72 / 8.0 = 9.0")
    assert(Mathings.power(2,3) == "2 ^ 3 = 8")
    assert(Mathings.power("hgslkfglqegf",62) == "Invalid input")
    assert(Mathings.pythagoras(12,5) == "c = 13.0")
    assert(Mathings.pythagoras(5,"0") == "Invalid input")
    assert(Mathings.getKthDigit(1639565693257,1) == "the 1th digit of 1639565693257 is 5")
test_assert()    
def main():
    """
    Runs asserts for the static methods in Mathings class
    
    
    """
    test_assert()    
if __name__ == "__main__":
    main()