import time
from random import randint

def TempSwap():
    
    begin = time.time()
    
    # Python program to demonstrate
    # swapping of two variables
    # using a temp variable
    
    counter = 0
    for i in range(1000): #loop to run 1000 instances
        x = randint(1, 1000) #random number from 1-1000
        y = randint(1, 1000) 

        # Swapping of two variables
        # Using third variable
        temp = x
        x = y
        y = temp
        counter += 1

        #print new values of x and y
        print("New value of x:", x)
        print("New value of y:", y)
        #print how many times the program has run
        print("The loop has ran", counter ,"times")
        
    #end timer
    end = time.time()
    #print total run-time
    print(f"Total runtime of the program is {end - begin}")
            
#call method
print(TempSwap())



    