import random
import time
import copy

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
    


def bubble_sort(arr):
    """
    a mutating sort
    sorts a list in asscending order
    
    Args:
        arr(list)
    return:
        list, sorted list
    """
    n = len(arr)
    
    if n <= 1:
        return arr
    for i in range(n):
        swapped = False # flag variable
        
        for j in range(0, n-i-1): # n = total num, i = total pases -1  so that we don't compare sorted items,
            if arr[j] > arr[j+1]:
                # x,y = y,x  (flip flop)
                arr[j], arr[j+1] = arr[j+1] ,arr[j]
                swapped = True #you did a swap
        
        if not swapped:# break
            break
                
    return arr


def insertion_sort(arr):
    """
    A mutating sort
    sorts a list in asscending order
    
    Args:
        arr(list)
    return:
        list, sorted list
    
    """
    array = copy.copy(arr)
    for i in range(1,len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j-1] # swap
            j -= 1
            
    return array
    
def binary_search(arr, target):
    """
    Performs an iterative binary search on a SORTED list.
    
    Arguments:
        array(list): a sorted list if nums
        target(int or float): the value to search for
    Example:
        binary_search([1,2,3,4,5,6,7,8,9], 6)
        >>> 5
        binary_search([1,3,5,7,9], 4)
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
    return -1 # can be str, boolean, etc 
    
def linear_search(array, target):
    """
    Performs an iterative linear search on a SORTED list.
    
    Arguments:
        array(list): a sorted list if nums
        target(int or float): the value to search for
    Example:
        linear_search([1,2,3,4,5,6,7,8,9], 6)
        >>> True
        linear_search([1,3,5,7,9], 4)
        >>> False    
    
    """
    for value in array:
        if value == target:
            return True
    return False    
    
def time_calc(func, arr, target=None):
    """
    A function that tests and prints how long it takes for a function to finish 
    the task.

    Arguments:
        func (function): a function to be run inside this function.
        arr (list): a data set of numbers.
        target (NoneType/int): optional argument for special edge/else cases.

    Example:
        time_calc(bubble_sort, [1, 7, 3, 4, 9, 10, 2])
        >>> 0.0000000322523
    """

    array = copy.copy(arr)  # Creates a copy of the input array to avoid modifying the original.

    if target is not None:  # Checks if a target argument is provided (used for searching functions).
        start = time.time()  # Records the start time before calling the function.
        func(array, target)  # Calls the function with the copied array and target value.
        end = time.time()  # Records the end time after function execution.

    else:  # If no target is provided, the function is assumed to work only with the array.
        start = time.time()  # Records the start time.
        func(array)  # Calls the function with just the copied array.
        end = time.time()  # Records the end time.

    delta = end - start  # Calculates the elapsed time for function execution.

    return delta  # Returns the elapsed time.


def test_run(length):
    """
    function is designed to generate random arrays of numbers and evaluate the performance of sorting and searching algorithms under certain conditions.
    It does this by timing how long it takes for each algorithm to complete its task and then printing the results.
    Arguments:
        length(int): length of the array
    Example:
        test_run(1000)
        >>> Unsorted Bubble time: 0.3360000656305237
        >>> Unsorted Insertion time: 0.287000778056757
        >>> Reverse Unsorted Bubble time: 0.3170001786370958
        >>> Reverse Unsorted Insertion time: 0.286999922380155
        >>> Double Unsorted Bubble time: 1.188999803144339
        >>> Double Unsorted Insertion time: 1.152000743113286
        >>> Sorted Bubble time: 0.00020003318786621094
        >>> Sorted Insertion time: 0.001799750084579467
        >>> Reverse Sorted Bubble time: 0.5200000187107462
        >>> Reverse Sorted Insertion time: 0.614000057620083
        >>> Double Sorted Bubble time: 0.7400000755125152
        >>> Double Sorted Insertion time: 0.5180009872306291
        >>> Sorted Inside Array Linear time: 0.00039997100830078124
        >>> Sorted Inside Array Binary time: 0.0
        >>> Reverse Sorted Inside Array Linear time: 0.0
        >>> Reverse Sorted Inside Array Binary time: 0.00020003318786621094
        >>> Double Sorted Inside Array Linear time: 0.00020003318786621094
        >>> Double Sorted Inside Array Binary time: 0.00039997100830078124
        >>> Sorted Outside Array Linear time: 0.00019998550415039062
        >>> Sorted Outside Array Binary time: 0.0
        >>> Reverse Sorted Outside Array Linear time: 0.0
        >>> Reverse Sorted Outside Array Binary time: 0.00019998550415039062
        >>> Double Sorted Outside Array Linear time: 0.00019998550415039062
        >>> Double Sorted Outside Array Binary time: 0.00020003318786621094
        >>> Sorted Random Array Linear time: 0.0
        >>> Sorted Random Array Binary time: 0.00019998550415039062
        >>> Reverse Sorted Random Array Linear time: 0.00020003318786621094
        >>> Reverse Sorted Random Array Binary time: 0.00019998550415039062
        >>> Double Sorted Random Array Linear time: 0.0
        >>> Double Sorted Random Array Binary time: 0.0
        #I'm sorry Mr. Hobbs
    """

    length = int(length)
    unsorted_arr = random_list(length,0,1000000)  # generates a list with random numbers
    double_unsorted_arr = unsorted_arr + unsorted_arr  # creates a Double Unsorted Array
    rev_unsorted_arr = unsorted_arr[::-1]  # creates a reversed version of the unsorted array
    sorted_arr = insertion_sort(unsorted_arr)  # sorts the array using insertion sort
    double_sorted_arr = sorted_arr + sorted_arr  # creates a Double Sorted Array
    
    rev_sorted_arr = sorted_arr[::-1]  # creates a reversed version of the sorted array

    # Random values for testing search algorithms
    randomInt = random.randint(0,1000000)
    randomIndex = random.randint(1,length) - 1
    randomItem = unsorted_arr[randomIndex]  # selects a random element from the array
    outsideNum = random.randint(1000000,1000000000)  # generates a number outside the array range
    
    # Bubble and Insertion Sort Performance Testing
    unsorted_bubble = time_calc(bubble_sort, unsorted_arr)
    unsorted_insertion = time_calc(insertion_sort, unsorted_arr)
    print(f"Unsorted Bubble time = {unsorted_bubble}")
    print(f"\nUnsorted Insertion time = {unsorted_insertion}")        
    
    rev_unsorted_bubble = time_calc(bubble_sort, rev_unsorted_arr)
    rev_unsorted_insertion = time_calc(insertion_sort, rev_unsorted_arr)
    print(f"\nReverse Unsorted Bubble time = {rev_unsorted_bubble}")
    print(f"\nReverse Unsorted Insertion time = {rev_unsorted_insertion}")
    
    double_unsorted_bubble = time_calc(bubble_sort, double_unsorted_arr)
    double_unsorted_insertion = time_calc(insertion_sort, double_unsorted_arr)
    print(f"\nDouble Unsorted Bubble time = {double_unsorted_bubble}")
    print(f"\nDouble Unsorted Insertion time = {double_unsorted_insertion}")
    
    sorted_bubble = time_calc(bubble_sort, sorted_arr)
    sorted_insertion = time_calc(insertion_sort, sorted_arr)
    print(f"\nSorted Bubble time = {sorted_bubble}")
    print(f"\nSorted Insertion time = {sorted_insertion}")
    
    rev_sorted_bubble = time_calc(bubble_sort, rev_sorted_arr)
    rev_sorted_insertion = time_calc(insertion_sort, rev_sorted_arr)
    print(f"\nReverse Sorted Bubble time = {rev_sorted_bubble}")
    print(f"\nReverse Sorted Insertion time = {rev_sorted_insertion}")
    
    double_sorted_bubble = time_calc(bubble_sort, double_sorted_arr)
    double_sorted_insertion = time_calc(insertion_sort, double_sorted_arr)
    print(f"\nDouble Sorted Bubble time = {double_sorted_bubble}")  
    print(f"\nDouble Sorted Insertion time = {double_sorted_insertion}")
    
    # Linear and Binary Search Performance Testing
    # Searching for an existing item inside sorted arrays
    sorted_linear_inside = time_calc(linear_search, sorted_arr, randomItem)
    sorted_binary_inside = time_calc(binary_search, sorted_arr, randomItem)
    print(f"\nSorted Inside Array Linear time = {sorted_linear_inside}")
    print(f"\nSorted Inside Array Binary time = {sorted_binary_inside}")            
    
    rev_sorted_linear_inside = time_calc(linear_search, rev_sorted_arr, randomItem)
    rev_sorted_binary_inside = time_calc(binary_search, rev_sorted_arr, randomItem)
    print(f"\nReverse Sorted Inside Array Linear time = {rev_sorted_linear_inside}")
    print(f"\nReverse Sorted Inside Array Binary time = {rev_sorted_binary_inside}")          
    
    double_sorted_linear_inside = time_calc(linear_search, double_sorted_arr, randomItem)
    double_sorted_binary_inside = time_calc(binary_search, double_sorted_arr, randomItem)
    print(f"\nDouble Sorted Inside Array Linear time = {double_sorted_linear_inside}")
    print(f"\nDouble Sorted Inside Array Binary time = {double_sorted_binary_inside}")          
    
    # Searching for an item that does not exist (outside the array range)
    sorted_linear_outside = time_calc(linear_search, sorted_arr, outsideNum)
    sorted_binary_outside = time_calc(binary_search, sorted_arr, outsideNum)
    print(f"\nSorted Outside Array Linear time = {sorted_linear_outside}")
    print(f"\nSorted Outside Array Binary time = {sorted_binary_outside}")
    
    rev_sorted_linear_outside = time_calc(linear_search, rev_sorted_arr, outsideNum)
    rev_sorted_binary_outside = time_calc(binary_search, rev_sorted_arr, outsideNum)
    print(f"\nReverse Sorted Outside Array Linear time = {rev_sorted_linear_outside}")
    print(f"\nReverse Sorted Outside Array Binary time = {rev_sorted_binary_outside}")
    
    double_sorted_linear_outside = time_calc(linear_search, double_sorted_arr, outsideNum)
    double_sorted_binary_outside = time_calc(binary_search, double_sorted_arr, outsideNum)
    print(f"\nDouble Sorted Outside Array Linear time = {double_sorted_linear_outside}")
    print(f"\nDouble Sorted Outside Array Binary time = {double_sorted_binary_outside}")      
    
    # Searching for a random number that may or may not be in the array
    sorted_linear_random = time_calc(linear_search, sorted_arr, randomInt)
    sorted_binary_random = time_calc(binary_search, sorted_arr, randomInt)
    print(f"\nSorted Random Array Linear time = {sorted_linear_random}")
    print(f"\nSorted Random Array Binary time = {sorted_binary_random}")
    
    rev_sorted_linear_random = time_calc(linear_search, rev_sorted_arr, randomInt)
    rev_sorted_binary_random = time_calc(binary_search, rev_sorted_arr, randomInt)
    print(f"\nReverse Sorted Random Array Linear time = {rev_sorted_linear_random}")
    print(f"\nReverse Sorted Random Array Binary time = {rev_sorted_binary_random}") 
    
    double_sorted_linear_random = time_calc(linear_search, double_sorted_arr, randomInt)
    double_sorted_binary_random = time_calc(binary_search, double_sorted_arr, randomInt)
    print(f"\nDouble Sorted Random Array Linear time = {double_sorted_linear_random}")
    print(f"\nDouble Sorted Random Array Binary time = {double_sorted_binary_random}")



    
def main():
    """
    
    function asks the user how long they want the array to be, and prints 5 itterations of 
    how long it takes for the test function to do something
    Example:
        main()
        Array Length: 1000
        >>> Unsorted Bubble time: 0.3360000656305237
        >>> Unsorted Insertion time: 0.287000778056757
        >>> Reverse Unsorted Bubble time: 0.3170001786370958
        >>> Reverse Unsorted Insertion time: 0.286999922380155
        >>> Double Unsorted Bubble time: 1.188999803144339
        >>> Double Unsorted Insertion time: 1.152000743113286
        >>> Sorted Bubble time: 0.00020003318786621094
        >>> Sorted Insertion time: 0.001799750084579467
        >>> Reverse Sorted Bubble time: 0.5200000187107462
        >>> Reverse Sorted Insertion time: 0.614000057620083
        >>> Double Sorted Bubble time: 0.7400000755125152
        >>> Double Sorted Insertion time: 0.5180009872306291
        >>> Sorted Inside Array Linear time: 0.00039997100830078124
        >>> Sorted Inside Array Binary time: 0.0
        >>> Reverse Sorted Inside Array Linear time: 0.0
        >>> Reverse Sorted Inside Array Binary time: 0.00020003318786621094
        >>> Double Sorted Inside Array Linear time: 0.00020003318786621094
        >>> Double Sorted Inside Array Binary time: 0.00039997100830078124
        >>> Sorted Outside Array Linear time: 0.00019998550415039062
        >>> Sorted Outside Array Binary time: 0.0
        >>> Reverse Sorted Outside Array Linear time: 0.0
        >>> Reverse Sorted Outside Array Binary time: 0.00019998550415039062
        >>> Double Sorted Outside Array Linear time: 0.00019998550415039062
        >>> Double Sorted Outside Array Binary time: 0.00020003318786621094
        >>> Sorted Random Array Linear time: 0.0
        >>> Sorted Random Array Binary time: 0.00019998550415039062
        >>> Reverse Sorted Random Array Linear time: 0.00020003318786621094
        >>> Reverse Sorted Random Array Binary time: 0.00019998550415039062
        >>> Double Sorted Random Array Linear time: 0.0
        >>> Double Sorted Random Array Binary time: 0.0
        #I'm sorry Mr. Hobbs
    """
    
    while True:
        user = input('Array Length: ')
        if user == 'stop':
            break
        num = int(user)
        for i in range(0,5):#test_run function runs 5 times.
            test_run(num)
        

    
    
    
            
            
    
main()            
