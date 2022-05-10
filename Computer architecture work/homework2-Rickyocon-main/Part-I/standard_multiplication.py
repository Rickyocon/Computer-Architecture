
# standard_multiplication.py

#Ricky 
#Multiplication of binary numbers
#Imports
from msilib.schema import Binary
import time
from random import randint
from xmlrpc.client import boolean

#Start timer
begin = time.time()

#---------------------------------------------------------------------------------------
#Functions
 
def standard_multiplication():

    #init counter to store amount of times program runs
    counter = 0
    #Loop the program 1000 times
    for i in range(1000): #loop to run 1000 instances
        multiplicand = randint(-1000, 1000) #random number from -1000-1000
        multiplier = randint(-1000, 1000)
        #inc counter
        counter += 1
        #binary conversion
        binary1 = format(multiplicand, "016b").replace("0b", "")
        binary2 = format(multiplier, "016b").replace("0b", "")
        #print values
        print ("--------------------------------------")
        
        #print values for multiplicand and multiplier
        #Print positive binary values for multiplicand and multiplier
        #Store a boolean value if value was a negitive
        print ("Multiplicand:",multiplicand)
        if multiplicand < 0:
            print ("Multiplicand converted to unsigned binary: ",binary1.replace("-", ""))
            #boolean flag to track if number was negitive
            multiplicandChanged = True
        else:
            print ("Multiplicand converted to binary: ",binary1)

        print ("Multiplier:",multiplier)
        if multiplier < 0:
            print ("Multiplier converted to unsigned binary: ",binary2.replace("-", ""))
            #boolean flag to track if number was negitive
            multiplierChanged = True
        else:
            print ("Multiplier converted to binary: ",binary2)
        print ("--------------------------------------")

        #Multiply positive binary values

        #binary addidition function
        strBinary1 = str(binary1)
        strBinary2 = str(binary2)
        
        #print(strBinary1)
        A = "0000000000000000"
        c = 0
        #arr = [c,A,strBinary2,strBinary1]
        binAdd(strBinary1,strBinary2)
        print("---------------------------------------")


        stringLength = len(strBinary1)
        revStrBinary2 = strBinary1[stringLength::-1]
        for i in range(len(strBinary2)):
            if strBinary2[0]=="1":
                A = binAdd(A,strBinary2)
                A.append(c.pop())
                c = 0
                revStrBinary2.append(A[0])
                A = A[1:len(A)]
                strMultiplicand = revStrBinary2[1:len(revStrBinary2)]
     
            


            
            
    print("Loop ran ",counter," times")

def binAdd(Val1,Val2):
    sum = bin(int(Val1, 2) + int(Val2, 2))
    sum = sum.replace("0b", "")
    if sum[0] == "-":
        sum = sum.zfill(17)
    sum = sum.zfill(16)
    print("Sum is: ",sum)

#-----------------------------------------------------------------------   
#Main     
standard_multiplication() 
#end timer
end = time.time()
#print total run-time
print(f"Total runtime of the program is {end - begin}")
                           
