seaCreatures = ['lobster','manta rays','octupus','pufferfish','salmon','sea horse','sea urchin','shrimp','squid','stingray']
category = ['Crustacean','Cartilaginous','Cephalopod','driving instructor','Fish','fish','Enchinoderm','good with prime rib','Squidward','ray that stings']





def binary_search(arr, target):
    """
    Performs an iterative binary search on a SORTED list.
    
    Arguments:
        array(list): a sorted list of sea creatures
        target(string): sea creature to search for in the list
    Example:
        binary_search(['lobster','manta rays','sea horse','sea urchin','squid'], squid)
        >>> 4
        binary_search(['lobster','manta rays','sea horse','sea urchin','squid'], clown fish)
        >>> -1
    """
    
    low = 0
    high = len(arr) - 1
    mid = 0
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

        
    #target not found
    return -1 # can be str, boolean, etc.


def fishAndCategory(arr1,arr2,user):
    """
    Performs a search between 2 paralel arrays that returns if the sea creature is in the array and what type of creature it is.
    
    Arguments:
        arr1(list): a sorted list of stuff.
        arr2(list): a sorted list of types of those stuff.
        user(string): the name of a sea creature that the function will search for
    Example:
        fishAndCategory(['lobster','manta rays','sea horse','sea urchin','squid'],['Crustacean','Cartilaginous','Fish','Enchinoderm','Squidward'], 'Lobster')
        >>> A lobster is a Crustacean
        fishAndCategory(['lobster','manta rays','sea horse','sea urchin','squid'],['Crustacean','Cartilaginous','Fish','Enchinoderm','Squidward'], 'Clown fish')
        >>> clown fish is not in the array, check your spelling.
        fishAndCategory(['lobster','manta rays','sea horse','sea urchin','squid'],['Crustacean','Cartilaginous','Fish','Enchinoderm','Squidward'], ' ')
        >>> That is not a valid input.    

        """

    
    result = binary_search(arr1,user) # search if the target seaCreature is inside the array
    index = 0 
    if user != '' : # if user has some text
        if result != -1: # if the value of result is not -1
            index = result # val of index becomes the val of result
            output1 = arr1[index].lower() # sets all of the letters in output1 to lowercase
            output2 = arr2[index].lower() # sets all of the letters in output2 to lowercase
            return  f"A {output1} is a {output2}\nType stop to stop." 
        return f"{user} is not in the array, check your spelling.\nType exit to exit." 
    return 'That is not a valid input'    



seaCreatures = ['lobster','manta rays','octupus','pufferfish','salmon','sea horse','sea urchin','shrimp','squid','stingray']
category = ['Crustacean','Cartilaginous','Cephalopod','driving instructor','Fish','fish','Enchinoderm','good with prime rib','Squidward','ray that stings']    
    
def main_loop(arr1,arr2):
    """
    The function asks the prints off everything in the first array, asks the user what fish/ocean creature they want, and returns the name of the fish/ocean creature
    that they typed and with what class they are(the class comes from the second array)
    
    Arguments:
        arr1(list): a sorted list of creatures in the sea.
        arr2(list): a sorted list of types of cretures in the sea.
        
    Example:
        fishAndCategory(['lobster','manta rays','sea horse','sea urchin','squid'],['Crustacean','Cartilaginous','Fish','Enchinoderm','Squidward'], 'Lobster')
        >>> A lobster is a Crustacean
        fishAndCategory(['lobster','manta rays','sea horse','sea urchin','squid'],['Crustacean','Cartilaginous','Fish','Enchinoderm','Squidward'], 'Clown fish')
        >>> clown fish is not in the array, check your spelling.
        fishAndCategory(['lobster','manta rays','sea horse','sea urchin','squid'],['Crustacean','Cartilaginous','Fish','Enchinoderm','Squidward'], ' ')
        >>> That is not a valid input.
    """
    for creature in seaCreatures:
        print(creature) #prints every item in seaCreatures array 
    
    while True:
        userInput = input('Chose your fish: ').strip() # asks the user what fish they want to enter
        userInput = userInput.lower()
        userInput = userInput.replace(" ","")# turns every letter in userInput to a lowercase leter
        if userInput == 'exit': # if the user enters stop, the loop stops.
            print('the function has stopped')
            break    
        print(fishAndCategory(arr1,arr2,userInput)) # the user enters anything else other than  stop, the function fishAndCategory is ran. 


main_loop(seaCreatures,category)


def test_assert(arr):
    """
    Performs asserts/check if the binary search acutually works
    
    Arguments
        arr(list): a sorted array / lists, containing creatures from the sea.
        
    Example:
        
        >>> # returns nothing because the aasert has passed
    """
    assert binary_search(arr,'lobster') == 0
    assert binary_search(arr,'manta ray') == -1
    assert binary_search(arr,'octupus') == 2
    assert binary_search(arr,'manta rays') == 1
    assert binary_search(arr,'pufferfish') == 3
    assert binary_search(arr,'salmon') == 4
    assert binary_search(arr,'sea horse') == 5
    assert binary_search(arr,'sea urchin') == 6
    assert binary_search(arr,'shrimp') == 7
    assert binary_search(arr,'squid') == 8
    assert binary_search(arr,'stingray') == 9
    assert binary_search(arr,' ') == -1
    assert binary_search(arr,'uetfrqwetdukaetfuioqwegf7owei') == -1
    
test_assert(seaCreatures)
    
    
    
    