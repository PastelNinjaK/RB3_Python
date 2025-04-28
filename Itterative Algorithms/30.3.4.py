import random

def random_list(length, min_val, max_val):
    """
    populates a list with random numbers based on the users input
    
    Arguments:
        length(int) = how long the user wants the array to be.
        min_val = the minimum val that can be insaide the array
        max_val = the maximum number that can be inside the array
    Example:
        print(random_list(5,6,20))
        >>>[17,19,15,15,11]
    """
    length = int(length) # ensures that length is a whole num/integer
    items = [random.randint(min_val, max_val) for _ in range(length)] #assigns random numbers for each index of the array/(index is equal to the val of length - 1)
    return items # returns items
    
def rev_bubble_sort(arr):
    """
    a mutating sort
    sorts a list in desscending order
    
    Args:
        arr(list)
    return:
        list, sorted list
    """
    
    n = len(arr) #items in array
    
    if n <= 1:
        return arr
    for i in range(n):
        swapped = False # flag variable
        
        for j in range(0, n-i-1): # n = total num, i = total pases -1  so that we don't compare sorted items,
            if arr[j] < arr[j+1]:#if it's not in order, switch
                # x,y = y,x  (flip flop)
                arr[j], arr[j+1] = arr[j+1] ,arr[j]
                swapped = True #you did a swap
        
        if not swapped:# break
            break
                
    return arr
    
def test_assert():
    """
    Performs asserts/check if the binary search acutually works
        
    Example:
        rev_bubble_sort([1,2,4,5,3,9]) == [9,5,4,3,2,1]
        >>> # returns nothing because the aasert has passed
    """
    
    assert rev_bubble_sort([4,9,5,7,1,3]) == [9,7,5,4,3,1]
    assert rev_bubble_sort([1,9,4,7,3,5]) == [9,7,5,4,3,1]
    assert rev_bubble_sort([2,4,6,8,10,12]) == [12,10,8,6,4,2]
    assert rev_bubble_sort([1,2,3,4,5,6,7,8,9]) == [9,8,7,6,5,4,3,2,1]
    assert rev_bubble_sort([3,6,9,12,15,18]) == [18,15,12,9,6,3]
    assert rev_bubble_sort([]) == []
    assert rev_bubble_sort([1]) == [1]
    assert rev_bubble_sort([0,4,7,1,9,13]) == [13,9,7,4,1,0]



def why_nested_if_sucks():
    """
    This function explains why nested if statements suck.
    """
    text = (
    'Nested if statments suck because the more we have of them,'+ 
    'the harder it is to read the code(and or explain it / make a psuedo code for it).'+
    '\nA popular way of avoiding if statmets is using the guard causes technique'+
    ' which takes in the negative condition and seperates the codintions from the functions.'+
    '\nThis method allows the code to look much cleaner and simpler to understand.')
    return text
    
test_assert()    
def main_loop():
    """
    function generates a list with an index of 49 and explains why nested if statements suck.
    
    """
    
    
    unsorted = random_list(50,0,1000)
    print(f'Unsorted Array: {unsorted}')
    sortedArr = rev_bubble_sort(unsorted)
    print(f"\nSorted Array: {sortedArr}")
    text = why_nested_if_sucks()
    print(f'\n{text}')





main_loop()    
    
