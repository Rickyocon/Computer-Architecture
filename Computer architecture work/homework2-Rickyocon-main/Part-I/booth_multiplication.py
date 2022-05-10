from itertools import product
import time
from random import randint
from bitstring import BitArray


begin = time.time()

productstr = "Product is = "

def booth(m, r, x, y):
	# Initialize
	totalLength = x + y + 1
	mA = BitArray(int = m, length = totalLength)
	A = mA << (y+1)
	S = BitArray(int = -m, length = totalLength)  << (y+1)
	P = BitArray(int = r, length = y)
	P.prepend(BitArray(int = 0, length = x))
	P = P << 1

	#Print inititial values
	print ("Initial values")
	print ("A", A.bin)
	print ("S", S.bin)
	print ("P", P.bin)
	print ("Starting calculation")

	#loop to multiply using booths algorithum (using arithetmic shifts)
	for i in range(1,y+1):
		if P[-2:] == '0b01':
			P = BitArray(int = P.int + A.int, length = totalLength)
			print ("P +  A:", P.bin)
		elif P[-2:] == '0b10':
			P = BitArray(int = P.int +S.int, length = totalLength)
			print ("P +  S:", P.bin)
		P = arith_shift_right(P, 1)
		print ("P >> 1:", P.bin)
	P = arith_shift_right(P, 1)
	print ("P >> 1:", P.bin)
	return productstr,P.int

#function to preform shifts used in the multiplication process
def arith_shift_right(x, amt):
	l = x.len
	x = BitArray(int = (x.int >> amt), length = l)
	return x

#Main
#run 1000 instances of the multiplication of 1000 randomly 16 bit generated values (- or +)
counter = 0;
for i in range(1000):
    x = 16
    y = 16
    m = randint(-1000, 1000)
    r = randint(-1000, 1000)
    print("-----------------------------------")
    print("Multiplicand: ",m)
    print("Multiplier: ",r)
    b = booth(m, r, x, y)
    print (b) 
    print("-----------------------------------")
    counter += 1

#Print the amount of times the loop ran
print("Loop has run",counter," times")
#calculate program run time
#end timer
end = time.time()
#print total run-time
print(f"Total runtime of the program is {end - begin}")
            