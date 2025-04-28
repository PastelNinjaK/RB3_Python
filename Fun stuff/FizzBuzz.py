
def FizzBuzz(num):
    array = list(range(1,num+1))
    print(array)
    for number in range(1,num + 1):
        div3 = number % 3
        div5 = number % 5 == 0
        if div3 == True and div5 == True:
            print('FizzBuzz')
        if div3 == True and div5 == False:
            print('Fizz') 
        if div5 == True:
            print('Buzz')
        else:
            print(number)
        
           
def main():
    FizzBuzz(50)





main()