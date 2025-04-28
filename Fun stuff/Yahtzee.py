import random

def rollDice(dice_array):
    """
    Rolls x amounts of dices

    Argumnets:
        dice_array(list): list of the dices (idgaf if this is the correct word, i just did this cuz I'm bored)
    Example:
        >>> rollDice(dice_array) 
        >>> '⚁' 
    """
    random_index = random.randint(0,5)
    random_dice = dice_array[random_index]
    return random_dice

def calculateScore(d1, d2, d3):
    """
    Calculates the score of the 3 dices
    final score is calculated as follows:

    Three of a kind → 20 + sum of all three dice
        Example: Rolling ⚃-⚃-⚃ → 20 + 4 + 4 + 4 = 32
    A pair → 10 + sum of the two matching dice
        Example: Rolling ⚃-⚃-⚂ → 10 + 4 + 4 = 18
    No matches → Score is just the highest die value
        Example: Rolling ⚂-⚄-⚁ → Score = 5


    Arguments:
        d1(str) = The first dice.
        d2(str) = The second dice.
        d3(str) = The third dice.
    
    Example:
        >>> print(calculateScore(⚀,⚃,⚀))
        >>> 12

    """
    dice_array = {'⚀':1,'⚁':2,'⚂':3,'⚃':4,'⚄':5,'⚅':6}
    d1_num = dice_array.get(d1)
    d2_num = dice_array.get(d2)
    d3_num = dice_array.get(d3)
    array = [d1_num,d2_num,d3_num]
    target = list(dice_array[item] for item in dice_array)
    counts_arr = []
    
    for item in target:
        result = array.count(item)
        counts_arr.append(result)
    score = 0
    if 3 in counts_arr:
        score = 20 + ((counts_arr.index(3) + 1) * 3)
        return score
    elif 2 in counts_arr:
        score = 10 + ((counts_arr.index(2) + 1) * 2)
        return score
    else:
        score = max(array)
        return score


def playThreeDiceYathzee():
    """
    Contains the main loop for the game.
    Example:

    Play Yathzee?(yes or no): yes
        >>> First roll: ⚀-⚃-⚀
        >>> Roll again?: yes
        >>> Re-roll: ⚀-⚅-⚀
        >>> Your score is 12

    """
    dice_array = ['⚀','⚁','⚂','⚃','⚄','⚅']
    while True:
        start = input("Play Yathzee?(yes or no): ").strip().lower().replace(' ','')
        if start != 'yes':
            print("Goodbye")
            break
        d1 = rollDice(dice_array)
        d2 = rollDice(dice_array)
        d3 = rollDice(dice_array)
        condition1 = (d1 == d2)# d1 and d2 are the same
        condition2 = (d2 == d3)# d2 and d3 are the same
        condition3 = (d3 == d1)# d3 and d1 are the same
        print(f'First roll: {d1}-{d2}-{d3}')

        if (condition1 == True and condition2 == True and condition3 == True):
            score = calculateScore(d1, d2, d3)
            print(f'Your score is {score}')
        elif condition1 == False and condition2 == False and condition3 == False:
            score = calculateScore(d1, d2, d3)
            print(f'Your score is {score}')
        else:
            roll_again = input('Roll again?: ').strip().lower().replace(' ','')
            
            if roll_again != "yes":
                score = calculateScore(d1, d2, d3)
                print(f'Your score is {score}')    
            if condition1 == True and condition2 == False:
                d3 = rollDice(dice_array)
                score = calculateScore(d1, d2, d3)
                print(f'Re-roll: {d1}-{d2}-{d3}')
                print(f'Your score is {score}')
            elif condition2 == True and condition3 == False:
                d1 = rollDice(dice_array)
                score = calculateScore(d1, d2, d3)
                print(f'Re-roll: {d1}-{d2}-{d3}')
                print(f'Your score is {score}')   
            else:
                d2 = rollDice(dice_array)
                score = calculateScore(d1, d2, d3)
                print(f'Re-roll: {d1}-{d2}-{d3}')
                print(f'Your score is {score}')   
                    
    


def main():
    playThreeDiceYathzee()



main()