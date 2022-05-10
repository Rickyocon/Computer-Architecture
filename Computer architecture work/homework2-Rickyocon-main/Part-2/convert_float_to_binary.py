from math import *
from random import randint
import random
import time

begin = time.time()

# main function: call fp(float number n different from 0)
def fp(n):
  # base-2 scientific notation
  global s,e,m
  s,e=0,0
  p=1
  if n<0:s=1
  if fabs(n)>=2:p=-1
  while(p*fabs(n)*pow(2,p*e))<p:
    e=e+1
  if p==-1 and fabs(n)!=2:e=e-1
  m=fabs(n)*pow(2,p*e)
  e=-1*p*e
  np=pow(-1,s)*m*pow(2,e)
 
  print("\nIEEE-754:")
  print("\nHalf precision (binary16):")
  # IEEE-754 half precision (binary16)
  binaryxx(15,5,10)
  print("\nSingle precision (binary32):")
  # IEEE-754 single precision (binary32)
  binaryxx(127,8,23)
  print("\nDouble precision (binary64):")
  # IEEE-754 double precision (binary64)
  binaryxx(1023,11,52)
  print("\nQuadrupule precision (binary128):")
  binaryxx(2047,15,112)

# IEEE-754 template
def binaryxx(eo,ed,md):
  print("S="+str(s),
      "\nE="+tobin(e+eo,ed)+" ("+str(e+eo)+")",
      "\nF="+tobin(round(modf(m)[0]*pow(2,md)),md)+
      " ("+str(round(modf(m)[0]*pow(2,md)))+")",
      "\nn="+str(pow(-1,s)*(1+round(modf(m)[0]*pow(2,md))/(pow(2,md)))*pow(2,e)))

# integer (n) to binary (b bits)
bits=[]
def tobin(n,b):
  bits.clear()
  np=n
  for c in range(b):
    if pow(2,b-1-c)<=np:
      bits.append(1)
      np=np-pow(2,b-1-c)
    else:
      bits.append(0)
  return "".join(str(i) for i in bits)


counter = 0
for i in range(1000):
    randInt = random.uniform(10.5, 75.5)
    fp(randInt)
    counter += 1
print("Loop ran ",counter," Times")
#end timer
end = time.time()
#print total run-time
print(f"Total runtime of the program is {end - begin}")