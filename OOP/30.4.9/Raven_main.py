from Raven_mathings import Mathings


def oppertaion(x = 0, y = 0):
    """
    contains all of the operation that the program may need to execute based on the input of the user

    Arguments:
        x(float): first number
        y(float): second number
    Example:
        oppertaion(2.5,1)
        >>> {'1.) Addition ': '2.5 + 1 = 3.5', '2.) Subtraction ': '2.5 - 1 = 1.5', '3.) Multiplication ': '2.5 * 1 = 2.5', '4.) Division ': '2.5 / 1 = 2.5', '5.) Pythagorean theorem': 'c = 2.692582403567252', '6.) Power': '2.5 ^ 1 = 2.5', '7.) Find the Kth Digit': 'the 1th digit of 2.5 is 0'}   
    
    """
    addition = Mathings.add(x,y) # returns the sum of x and y
    subtraction = Mathings.subtract(x,y) # returns the difference of x and y
    multiply =  Mathings.multiplication(x,y) # returns the product of x and y
    divide = Mathings.divide(x,y) # returns the quotient of x and y
    pytha = Mathings.pythagoras(x,y) # Takes x and y and uses the pythagorean theorem to find the third number.
    power = Mathings.power(x,y) # Takes x number and raises it to the power of y.
    kthDigit = Mathings.getKthDigit(x,y) # finds the yth digit of number x.
    short_1 = Mathings.short1() # Explanation of static method  
    short_2 = Mathings.short2() # The purpose of the @staticmethod decorator
    short_3 = Mathings.short3() # The difference between a static method and an instance method   
    
    options_library = {"1.) Addition ":addition,
                  "2.) Subtraction ": subtraction,
                  "3.) Multiplication ": multiply,
                  "4.) Division ":divide,
                  "5.) Pythagorean theorem": pytha,
                  "6.) Power": power,
                  "7.) Find the Kth Digit": kthDigit,
                  "8.) Short1": short_1,
                  "9.) Short2": short_2,
                  "10.) Short3": short_3}
    return options_library




def main():
    """
    Runs the main program

    Example:
        
        Caclulator porgram
        1.) Addition 
        2.) Subtraction 
        3.) Multiplication 
        4.) Division 
        5.) Pythagorean theorem
        6.) Power
        7.) Find the Kth Digit
        8.) Short1

        Choose your operation (1-7): 2
        2.) Subtraction 
        Type in the first number: 3
        Type in the second number: 4

        3.0 - 4.0 = -1.0

    
    """
    titles = ["\nCaclulator porgram",
                  "1.) Addition ",
                  "2.) Subtraction ",
                  "3.) Multiplication ",
                  "4.) Division ",
                  "5.) Pythagorean theorem",
                  "6.) Power",
                  "7.) Find the Kth Digit",
                  "8.) Short1",
                  "9.) Short2",
                  "10.) Short3",
                  "11.) Stop(type stop)"]
    

    while True:
        for item in titles:
            # Prints the contents of titles
            print(item)
        #Asks the user for a number     
        user =  input("\nChoose your operation (1-10) or (type stop to stop): ").strip().replace(" ","")
        if user == "stop" or user == '11':
            # if user inputs/types stop, program stops.
            break        
        if user not in '12345678910' or user == '':
            # if user inputs/types nothing or a letters except for stop, program prints "Not valid"
            print("Not valid")
            continue
        # Converts the user input to an integer and subtract 1 to get the index
        indx = int(user) - 1
        # Check if the selected index is out of range of the 'titles' list
        if indx > len(titles) - 1:
            print(f"Operation {indx} is not part of this calculator's OS ")
            continue
        # Gets and prints the name of the operation from the 'titles' array
        op = titles[indx + 1]
        print(titles[indx + 1])        
        try:
            if indx + 1 > 7:
                # if index + 1 > 7 program just prints the term for that corresponding index
                # This is for the short responses
                results_arr = oppertaion()
                ans =  results_arr.get(op)
                print(f"\n{ans}")

            else:
                # Asks the user for the first number
                number1 = input("Type in the first number: ")
                # Asks the user for the second number
                number2 = input("Type in the second number: ")
                # turns the 2 numbers from str to float.
                # Float and not int because int will get rid of any decimals that the user might input.
                num1 = float(number1)
                num2 = float(number2)
                results_arr = oppertaion(num1,num2)
                # Retrieve and prints the result of the selected operation
                ans =  results_arr.get(op)
                print(f"\n{ans}")

        except ValueError:
            #if there is a ValueError program returns this
            print("Please type in an actual number")
        



if __name__ == "__main__":
    main()