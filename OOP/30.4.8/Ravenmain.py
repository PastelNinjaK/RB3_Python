from Ravencoin import Coin 
#only imports the Coin class from coin.py file

def total_val(arr):
    """
    calculates the total amount in cents of coins inside the array parameter
    Arguments:
        arr(list): an array
    Example:
        >>> total_val( [
        Coin("Nickel",10.6,"Nickel-plated steel",5),
        Coin("Penny",12.7,"Copper-plated steel ",1),
        Coin("Dime",9.5,"Nickel-plated steel",10),
        Coin("Quarter",13.5,"Nickel-plated steel",25),
        Coin("Loonie",13.5,"Nickel-plated steel",100)
        ]) 
        >>> 141
    
    """
    val = 0
    for item in arr:
        val += item.in_cents
    return val
    

def test_assert(arr,ref):
        """
        checks if the total__val function works
        
        Arguments:
            arr(list): array of coins
            ref(int): the theoretical total value of coins inside arr parameter
        
        """
        test_ref = total_val(arr)
        assert(test_ref == ref)

def main():
    """
    Asks a user for a coin name, checks if the coin name is in the data base and returns the value(in cents), surface area, circumference,
    and material used to create said coin


    Example:
        >>> Coin name? Loonie

            The Loonie is made out of Nickel-plated steel and has a value of 100 cents.
            The surface area of one side of a Loonie is 572.5552611167398mm^2.
            A Loonie has a circumference of 84.82300164692441mm.
            The total value of coins in the array is equal to 141 cents.

                    
    
    
    """
    all_coins = [
        Coin("Nickel",10.6,"Nickel-plated steel",5),
        Coin("Penny",12.7,"Copper-plated steel ",1),
        Coin("Dime",9.5,"Nickel-plated steel",10),
        Coin("Quarter",13.5,"Nickel-plated steel",25),
        Coin("Loonie",13.5,"Nickel-plated steel",100)
    ]
    

    
    test_assert(all_coins,141)
    # Finds the names of the coin and puts them inside an array
    coin_names = []
    for item in all_coins:
        coin_names.append(item.coin_name.lower())
    for name in coin_names:
        print(name)   


    
    
    # UI
    user = ""
    while True:
        user = input("Choose your coin?(Type stop to stop) ").strip().lower().replace(" ","")
        if user == 'stop':
            # if user types stop, main loop is terminated and prints bye.
            print("bye")
            break
        if user not in coin_names:
            # if the user inputs a name /text that is not in the data base, function asks the question again.
            print("The coin that you are looking for is not in my data base.\nPlease try again.")
            continue
        # finds the index of the coin name from coin_names array.
        indx = coin_names.index(user)
        #prints the instances for the coin chosen by the user
        print(all_coins[indx])
        total = total_val(all_coins)
        #prints the total value (in cents) of the coins in all_coins array.
        text = f"The total value of coins in the array is equal to {total} cents."
        print(text)    
            

if __name__ == "__main__":
    main()


