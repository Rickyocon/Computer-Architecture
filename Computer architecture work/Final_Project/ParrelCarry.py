#Imports
import random
import time

#Function to convert decimal to binary
def decToBin(num):
    return bin(num).replace("0b", "")


#Function that adds two binary numbers using the ripple carry method
def rippleCarry(binNum1,binNum2):
    start_time1 = time.time()
    max_len = max(len(binNum1), len(binNum2))
    binNum1 = binNum1.zfill(max_len)
    binNum2 = binNum2.zfill(max_len)

    # Initialize the result
    result = ''
    # Initialize the carry
    carry = 0
    # Traverse the string
    cycles1 = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if binNum1[i] == '1' else 0
        r += 1 if binNum2[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        # Compute the carry.
        carry = 0 if r < 2 else 1
        cycles1 += 1
    if carry != 0:
        result = '1' + result
        cycles1 += 1

    end_time1 = time.time()
    return (result.zfill(max_len),end_time1 - start_time1,cycles1)




#Function that adds two binary numbers using the parallel carry method
def parallelCarryHelper(BinaryNum1,BinaryNum2,cycles2):
    start_time2 = time.time()
    max_len = max(len(BinaryNum1), len(BinaryNum2))
    BinaryNum1 = BinaryNum1.zfill(max_len)
    BinaryNum2 = BinaryNum2.zfill(max_len)
    carry_number = "0"
    sum = ""
    for i in range(1,max_len+1):
        carry_over = (int(BinaryNum1[len(BinaryNum1)-i])) + (int(BinaryNum2[len(BinaryNum2)-i]))
        if carry_over == 0:
            sum += "0"
            carry_number += "0"
        elif carry_over == 1:
            sum += "1"
            carry_number += "0"
        elif carry_over == 2:
            sum += "0"
            carry_number += "1"
    sum = sum[::-1]
    carry_number = carry_number[::-1]
    cycles2 += 1
    if carry_number != "0"*(max_len+1):
        return parallelCarryHelper(sum,carry_number,cycles2)

    end_time2 = time.time()
    return (sum, end_time2 - start_time2,cycles2)

def parallelCarry(BinaryNum1,BinaryNum2):
    cycles2 = 0
    return parallelCarryHelper(BinaryNum1,BinaryNum2,cycles2)


    
#main
def main():
    
    counter = 0
    for i in range(10):
        
        #decToBin
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, 1000)
        print("=====================================================================================")
        print("First number pre-conversion: ",num1)
        print("Second number pre-conversion: ",num2)
        
        #initialize
        num1 = decToBin(num1)
        num2 = decToBin(num2)
        print("First number after being converted: ",num1)
        print("Second number after being converted: ",num2)
        
        
        #rippleCarry
        #initialize
        binNum1 = str(num1)
        binNum2 = str(num2)
        (answer1,time1,cycles1) = rippleCarry(binNum1,binNum2)
        print("Sum of binary numbers calculated via the ripple carry method: ",answer1)
        print("Time to calculate binary addition using ripple carry method: ", time1)
        print("The Ripple carry method took",cycles1,"cycles to complete")
        
        
        #parallelCaryy
        #initalize
        BinaryNum1 = binNum1
        BinaryNum2 = binNum2
        (answer2,time2,cycles2) = parallelCarry(BinaryNum1,BinaryNum2)
        print("Sum of binary numbers calculated via the Parallel carry method: ",answer2)
        print("Time to calculate binary addition using parallel carry method: ", time2)
        print("The Parallel carry method took",cycles2,"cycles to complete")
        
        
        #time calculation
        if(time1 > time2):
            print("The parallel carry method was faster")
        if(time1 < time2):
            print("The Ripple carry method was faster")
        else:
            print("Both methods calculated the operation at the same time")
        
            
        #cycle calculation
        if(cycles1 > cycles2):
            print("Ripple carry took more cycles")
        elif(cycles1 < cycles2):
            print("Parallel carry took more cycles")
        
        
        
        print("=====================================================================================")
        

        
        counter += 1
    print("The Loop has run", counter," Times")
   
#main
    
#Call to main
if __name__=="__main__":
    main()