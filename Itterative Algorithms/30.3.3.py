


def closest_binary_search(arr, target):
    """
    Performs an iterative binary search on a SORTED list but unlike the standard, this function will return the closest value.
    
    Arguments:
        array(list): a sorted list if nums
        target(int or float): the value to search for
    Example:
        binary_search([1,2,3,4,5,6,7,8,9], 6)
        >>> 5
        binary_search([1,3,5,7,9], 4)
        >>> 4
    """
    
    low = 0
    high = len(arr) - 1
    mid = 0
    if arr[0] > target:
        return -1
    if arr[high] < target:
        return -2
        
        
    while low <= high:
        mid = ((high + low))//2 # Finds the average for mid point
        
        if arr[mid] == target:
            return mid
        #if target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        #if target is greater, ignore right half
        
        else:
            high = mid - 1

    # if there is no match, the function will return the closest value it can find to the target

    if abs(arr[low] - target) < abs(arr[high] - target): # if the abs of low index - target is less than abs of high index - target
        return low # function returns lowIndex
    return mid #else function returns mid index



def pay(heroPay, hours):
    """
    Performs a mathimatical calculation that returns the fee for the superhero's services.
    Arguments:
        heroPay(float/int): The price per hour of the hero that the user wants to hire.
        hours(float/int): The time that the hero's presence is required.
    
    Example:
        pay(0, 8)
        >>> Your total fee is: $0 
            Type exit to leave store
        pay(80,9)
        >>> Your total fee is: $864.0 
            Type exit to leave store
        pay(76,12)
        >>> Your total fee is: $1094.4 
            Type exit to leave store
        
    """
    flat = 0 # the flat rate
    taxPercent = 0.2 # tax flat fee for insurance
    tax = 0 
    if hours <= 0:# if the hours parameter is less than or equal to 0, 
        return 0  #function returns 0
    if hours <= 3: # if the hours parameter is less than or equal to 3,
        flat = (heroPay * 3) # flat rate is equal to 3 hour of work (ie. heroPay * 3)
        tax = (heroPay * 3) * taxPercent # calculated value of the tax for the superhero's Insurance
    else: #if the hours parameter is more than 3
        tax = (heroPay * hours) * taxPercent # calculated value of the tax for the superhero's Insurance
        flat =  (heroPay * hours)# flat rate is equal to the hero's pricce per hour multiplied by how many hours the hero needs to work   
    payment = flat + tax #payment is equal to the val of flat + the val of tax                
    return(f"Your total fee is: ${payment}\nType exit to leave store") # this will print Your total fee is: (payment) Type exit to leave store
                    
                    
        


    
def main_loop(arr1, arr2, arr3):
    """
    
    Functions asks for what power level is required to solve the user's problem, how long does the superhero have to work and returns
    the Alberta labour laws appiclable, and the total fee.
    
    Arguments:
        arr1(list): a sorted list of the power scale of each supperhero.
        arr2(list): a list of superhero names.
        arr3(list): a list of the price per hour of each superhero.
    Example:
        if power scale == 7.4 && if hours = 8
        Welcome to Superheroes for hire!
        On a scale of 1 - 9.99, What is the level of the hero you need: 7.4
        >>> You have chosen to hire hero Starlord
        the price per hour is: $150
        how many hours will you need your hero: 8
        >>> Accoriding to Alberta labour laws, Starlord is entitled to a 30 minute paid/unpaid break.
        >>> Your Total fee is $1140.0
            type exit to leave the store
        
        if power scale  == 19 && hours == 6:
        
        Welcome to Superheroes for hire!
        On a scale of 1 - 9.99, What is the level of the hero you need: 19   
        >>> I'm sorry, we do not have a hero with that much power.
        
        
        if power scale == 1 && hours == 7:
        Welcome to Superheroes for hire!
        On a scale of 1 - 9.99, What is the level of the hero you need: 1
        >>>I'm sory, we do not have for your task, please come back when you have bigger problems
        
        if power scale == 7.4 && hours == 0:
        Welcome to Superheroes for hire!
        On a scale of 1 - 9.99, What is the level of the hero you need: 7.4
        >>> You have chosen to hire hero Starlord
        the price per hour is: $150
        how many hours will you need your hero: 8
        >>> Goodluck
    """
    print('Welcome to Superheroes for hire!')
    while True:
        
        user = input('On a scale of 1 - 9.99, What is the level of the hero you need: ') # asks the user what power scale they need
        stop = ' '
        law = ''
        user = user.strip()
        if user == 'exit' or user == "" : # if the user every enters exit, the function stops
            print('Goodluck') 
            break            
        
        index = closest_binary_search(arr1,float(user))# runs a binary search and returns an index
        if index == -2: # if index is -1 or -2 \, function returns returns these 2 texts
            print("I'm sorry, we do not have a hero with that much power.")                    
        elif index == -1:
            print("I'm sory, we do not have for your task, please come back when you have bigger problems")
                
        else:# if index is not -1 or -2, function continues as intended
            heroName = arr2[index] # assigns the variable heroName to the name of the hero that the user will be hiring to solve their problem.
            heroPay = arr3[index] # assigns the variable heroPay to the price per hour of the hero that the user will be hiring to solve their problem.
            print(f'You have chosen to hire hero {heroName} \nthe price per hour is: ${heroPay}.')# prints 
            # 'You have chosen to hire hero + heroName 
            # the price per hour is: $ + heroPay.
            hours = input('how many hours will you need your hero: ') # asks the user how long the hero's presence is required.
            hours = int(hours) # turns hours into int
            if hours > 12: #if hours is greter than 12
                # function tells, user that it is a violation of Alberta labour laws asks tells the user to place a new val for hours
                print(f'According to Alberta Labour laws, {heroName} is not allowed to work for more than 12 hours. Please try again')  
                hours = int(input('how many hours will you need your hero: '))                 

            elif hours == 0:
                # hours = 0 function stops
                print('Goodluck')
                break
            elif hours <= 5:
                #if hours is greater than or equal to 5, function print accompaniying labour law
                law = (f'Accoriding to Alberta labour laws, {heroName} is not entitled to a break')
            elif hours > 5 and hours < 10:
                #if hours is greater than or equal to 5 but less than 10, function print accompaniying labour law
                law = (f'Accoriding to Alberta labour laws, {heroName} is entitled to a 30 minute paid/unpaid break.')
            else:
                #if hours is greater than or equal to 10 but less than 12, function print accompaniying labour law

                law = (f'Accoriding to Alberta labour laws, {heroName} is entitled to two 30 minute paid/unpaid break.')

    
            print (law)
            print(pay(arr3[index],hours))


name = ['Black Widow','Hawkeye','Starlord','Hulk','Spiderman','Captain America','Iron an','Batman','Thor','Doctor Starnge','Scarlet Witch','The Writers']
power = [6.0, 6.5, 7.5, 8.0, 8.45, 8.6, 8.9, 9.0, 9.1, 9.3, 9.5, 9.99]
pricePerHour = [70, 80, 150, 60, 0, -90, 270, 0, 100, 200,90, 1]

def test_assert(arr):
    """
    Performs asserts/check if the binary search acutually works
    
    Arguments
        arr(list): a sorted array / lists, containing creatures from the sea.
        
    Example:
        
        >>> # returns nothing because the aasert has passed
    """
    assert closest_binary_search(arr, 6) == 0
    assert closest_binary_search(arr, 6.5) == 1
    assert closest_binary_search(arr, 7.5) == 2
    assert closest_binary_search(arr, 8.0) == 3
    assert closest_binary_search(arr, 8.45) == 4
    assert closest_binary_search(arr, 8.6) == 5
    assert closest_binary_search(arr, 8.9) == 6
    assert closest_binary_search(arr, 9.0) == 7
    assert closest_binary_search(arr, 9.1) == 8
    assert closest_binary_search(arr, 9.3) == 9    
    assert closest_binary_search(arr, 9.5) == 10
    assert closest_binary_search(arr, 9.99) == 11
    assert closest_binary_search(arr, 6.2) == 1
    assert closest_binary_search(arr, 10) == -2
    assert closest_binary_search(arr, 4) == -1
    assert closest_binary_search(arr, 9.6) == 11
    assert closest_binary_search(arr, 8.2) == 4
    assert closest_binary_search(arr, 7.2) == 2



test_assert(power)
main_loop(power, name, pricePerHour)
