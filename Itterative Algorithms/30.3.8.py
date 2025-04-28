import random
import copy

def deck_of_cards(numbers,face,suits):
    """
    creates a suit of cards
    
    Arguments:
        numbers(list): an array of numbers from 1-9
        face(list): an array for the face cards (King,Queen,Jack,Aces)
        suits(string): symbol for the cards
        
    Example:
        print(deck_of_cards([1, 2, 3, 4, 5, 6, 7, 8, 9],['J','Q','K','A'],♥))
        >>> ['♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K', '♥A']   
    
    """
    # Create copies to avoid modifying the original list
    num_array = copy.copy(numbers)
    face_array = copy.copy(face)
    # Adss the symbols to the face and number cards
    for num in range(len(num_array)):
        num_array[num] = suits + str(num+2)
    for face in range(len(face_array)):
        face_array[face] =  suits + face_array[face] 
    # returns an array with face and num cards with symbols
    return num_array + face_array



def random_hand(arr,repeat = 1):
    """
    Generates a random hand filled with a length between 1-13
    Arguments:
        arr(list): array of the cards in the deck
        repeat(int): optional parameter,(how many random hand I want in 1 hand)
    Example:
        print(random_hand(['♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', 
        '♠Q', '♠K', '♠A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', 
        '♥K', '♥A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K', 
        '♣A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K', '♦A'],1))
        >>> ['♥2', '♦Q', '♦K', '♠J', '♠8'] 
        
    """
    # Create copies to avoid modifying the original list
    copy_of_deck = copy.copy(arr)
    # Generates a random int
    random_length = random.randint(1,13)
    # creates an array with a random length
    array = list(range(random_length))
    
    for i in range(repeat):
        for num in range(random_length):
            # Pick a random index from the deck copy
            rand_index = random.randint(0,len(copy_of_deck)-1)
            # Assign the selected element to the array and remove it from the deck copy
            array[num] = copy_of_deck.pop(rand_index)
    return array# Return the shuffled array


def shuffle(data):
    """
    
    A function that shuflles the contents of the array
    (I did not read the python documentation for random before making this function.
    Like always, I suffered for nothing.)
    
    Arguments:
        data(list): array filled with elements
    Example:
    >>> shuffle([1, 2, 3, 4, 5])
    >>> [3, 1, 5, 2, 4]

    """
    # Create copies to avoid modifying the original list
    length = len(data)
    arr = copy.copy(data)
    array = copy.copy(data)
    # Shuffle the array by randomly selecting indices
    for num in range(len(arr)):
        rand_index = random.randint(0,len(arr)-1)
        array[num] = arr.pop(rand_index)
    return array # returns array

def counts(string,target):
    """
    A function that counts how many times sothing has appeared on sothing else
    
    Arguments:
        string(string): a string that will serve as the reference(the one to be search for)
        target(string): the target
    Example:
        counts('1234564','4')
        >>> 2
        
    
    """
    return string.count(target)
 



def card_repeat(arr,suits,table):
    """
    Counts how many time a certain card appears in a hand
    
    Arguments:
        arr(list): an array with the cards from a hand
        suits(array): an array suits in a deck of cards
        table(arr): table of values to bee searched for
    Example:
        print(card_repeat(['♥4','♠4','♦4','♣4'],['♥','♠','♦','♣'],['2','3','4','5','6','7','8','9','10','J','Q','K','A']))
        >>> [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
    """
    # Create a copy of the input array to avoid modifying the original

    array = copy.copy(arr)
    # Remove suit symbols from the card values
    for suit in suits:
        array = [symbol.replace(suit,'') for symbol in array]
    # adds the card values into a single string       
    text = ''
    for item in array:
        text += str(item)

    # Count how many times each card value appears from the table
    return_arr = []
    for item in table:
        times = counts(text,item)
        return_arr.append(times)
 
    return return_arr    
    
def repeats(arr,target,table):
    """
    Returns which element in an array x amount of times in an array
    
    Arguments:
        arr(list): list of how many time a certain card appears in a hand
        target(int): minimum amount / repeat required
        table(arr): table of values to be searched for
    Example:
        print(repeats([0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],2,['2','3','4','5','6','7','8','9','10','J','Q','K','A']))
        >>> ['4']


        
    """
    # Create a copy of the input array to avoid modifying the original
    array = arr[:]
    # Replace elements that don't meet the target count with None
    for element in array:
        if element < target:
            index = array.index(element)
            array.pop(index)
            array.insert(index,None)
    # Collect indices of elements that met the target count
    index_arr = []
    index = 0
    for val in array:
        if val != None:
            index_arr.append(index)
        index+=1
    #If target count is not met, function returns none.
    if len(index_arr) == 0:
        return None
    return_arr = []
    # Map indices to their corresponding values in the table
    for num in index_arr:
        return_arr.append(table[num])
    return return_arr


def check(arr,suits,table):
    """
    Checks various the properties of a given hand.
    
    Arguments:
        arr (list): A list of card values.
        suits (list): A list of corresponding suits for the cards.
        table(arr): table of values to bee searched for
    
    Example:
        print(check(['♣5', '♣8', '♣4', '♥8', '♦10'],['♥','♠','♦','♣'],['2','3','4','5','6','7','8','9','10','J','Q','K','A']))
        >>> ['Same num: False', "Shuffled Hand:\n['♣4', '♥8', '♣8', '♦10', '♣5']", 'Three of a kind: None', "Three of a kind: None\nPair of: ['8']\nFour of a kind: None", 'Highest Pair: 8']
    """
    # Checks if all numbers are the same in the hand

    if len(arr) < 4:
        same_num = None
    same_num = repeats(card_repeat(arr, suits,table), len(arr),table)
    # Shuffles the hand for randomness
    shuffled = shuffle(arr)
    
    # Checks for three of a kind
    three_of_a_kind = repeats(card_repeat(arr, suits,table), 3,table)
    
    # Checks for pairs
    pairs = repeats(card_repeat(arr, suits,table), 2,table)
    
    # Checks for four of a kind
    four_of_a_kind = repeats(card_repeat(arr, suits,table), 4,table)
    
    # Determine the highest pair if any pairs exist
    highest_pair = 0
    if pairs is not None:
        highest_pair = max(pairs)
    
    # Format and return results
    return_arr = [
        f'Same num: {same_num}',
        f'Shuffled Hand:\n{shuffled}',
        f'Three of a kind: {three_of_a_kind}',
        f'Three of a kind: {three_of_a_kind}\nPair of: {pairs}\nFour of a kind: {four_of_a_kind}',
        f'Highest Pair: {highest_pair}'
    ]
    return return_arr

def main():
    """
    Generates 4 hands and asks the user which hand to test and what function to trst for.
    
    Arguments:
        None
    Example:
        >>> Generate a Hand? yes
            Hand 1:
            ['♥2', '♣Q']
            Hand 2:
            ['♥Q', '♠9', '♦Q', '♦8', '♠10', '♠A']
            Hand 3:
            ['♥A', '♦7']
            Hand 4:
            ['♦10']
            Press 1 for hand 1
            Press 2 for hand 2
            Press 3 hand 3
            Press 4 for hand 4
            Which hand do you want to test: 2
            Hand to test: ['♥Q', '♠9', '♦Q', '♦8', '♠10', '♠A']
            To if all cards on the hand are equal, press 1
            To shuffle, press 2
            to check 3 of a kind, press 3
            to check for pairs, press 4
            to check for highest pair press 5
            What Function to test(Type stop to try a new hand): 4
            Your chosen hand:
            ['♥Q', '♠9', '♦Q', '♦8', '♠10', '♠A']
            Three of a kind: None
            Pair of: ['Q']
            Four of a kind: None
    
    """
    #Decks array
    suits = ['♥','♠','♦','♣']
    nums = list(range(1,10))
    faces = ['J','Q','K','A']
    # Generates the deck
    hearts = deck_of_cards(nums,faces,'♥')
    spades = deck_of_cards(nums,faces,'♠')
    diamonds = deck_of_cards(nums,faces,'♦')
    clubs = deck_of_cards(nums,faces,'♣')
    the_deck = spades + hearts + clubs + diamonds
    # acceptable answers
    acceptable = ['yes','go','no']
    user_int = '' 
    while True:
        #Asks the user if they want to genrate a hand
        user_int = input('Generate a Hand? ').strip().lower().replace(' ','')
        # Until the user input is in acceptable array function asks again.
        while user_int not in acceptable:
            print('Invalid input.\nPlease try again.')
            user_int = input('Generate a Hand? ').strip().lower().replace(' ','')
        # if user input is == 'no', function stops
        if user_int == 'no':
            break
        # genrates an array with 4 things
        hand = list(range(4))
        # creates 4 hands
        for item in hand:
            hand[item] = random_hand(the_deck,4)
            print(f'Hand {item+1}:\n{hand[item]}')
        #instructions
        options = ['Press 1 for hand 1','Press 2 for hand 2','Press 3 hand 3','Press 4 for hand 4']
        # acceptable answers
        acceptable_arr = ['1','2','3','4','stop'] 
        for item in options:
            #prints the instructions
            print(item)
        
        user_input = ''
        
        while True:
            # Aks user which hand to test.
            user_input = input('Which hand do you want to test: ').strip().lower().replace(' ','')
            #if user input == stop, function resets to the first while loop

            # Until the user input is in acceptable array function asks again.        
            while user_input not in acceptable_arr:
                if user_input == 'stop':
                    break
                print('Invalid input.\nPlease try again.')
                user_input = input('Which hand do you want to test: ').strip().lower().replace(' ','')
            if user_input == 'stop':
                break
            
            
            
            
            index = int(user_input)-1
            # prints the user selected hand 
            print(f'Hand to test: {hand[index]}')
            # instructions
            function_options = ['To if all cards on the hand are equal, press 1','To shuffle, press 2','to check 3 of a kind, press 3',
            'to check for pairs, press 4','to check for highest pair press 5']
            indexs = ['1','2','3','4','5','stop']
            for choice in function_options:
                # Prints instructions
                print(choice)
            function = ' '
            while True:
                # asks user what properties to test for
                function = input("What Function to test(Type stop to try a new hand): ").strip().lower().replace(' ','')
                
                if function == 'stop':
                    break
                #if user input == stop, function resets to the second while loop                
                while function not in indexs:
                    print('Invalid input.\nPlease try again.')
                    function = input(f"What Function to test(Type stop to try a new hand): ").strip().lower().replace(' ','')
                    print(function)
                if function == 'stop':
                    break
                table = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']  
                #tested properties array
                result = check(hand[index],suits,table)
                function = int(function) - 1
                #prints the index containing the user chosen 
                print(f'Your chosen hand:\n{hand[index]}')
                print(result[function])
    print("Have a nice day!")

def test_asserts():
    """
    Performs asserts/check if the binary search acutually works
        
    Example:
        rev_bubble_sort([1,2,4,5,3,9]) == [9,5,4,3,2,1]
        >>> # returns nothing because the aasert has passed
    """    
    suits = ['♥','♠','♦','♣']
    numbers = list(range(1, 10))
    faces = ['J', 'Q', 'K', 'A']
    table = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    
    # Test deck_of_cards
    deck = deck_of_cards(numbers, faces, '♥')
    assert len(deck) == 13, "deck_of_cards failed"
    assert '♥2' in deck and '♥A' in deck, "deck_of_cards failed"
    
    # Test random_hand
    hand = random_hand(deck, 1)
    assert 1 <= len(hand) <= 13, "random_hand failed"
    

    
    # Test shuffle
    shuffled_deck = shuffle(deck)
    assert sorted(shuffled_deck) == sorted(deck), "shuffle failed"
    
    # Test counts
    assert counts("1234564", "4") == 2, "counts failed"
    
    # Test card_repeat
    hand1 = ['♥4','♠4','♦4','♣4']
    assert card_repeat(hand1, suits, table)[2] == 4, "card_repeat failed"
    
    # Test repeats
    assert repeats([0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 2, table) == ['4'], "repeats failed"
    
    # Test check
    check_result = check(['♣5', '♣8', '♣4', '♥8', '♦10'], suits, table)
    assert isinstance(check_result, list) and len(check_result) == 5, "check failed"
    


test_asserts()
main()    
