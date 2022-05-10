//Method to swap using a temp variable


#include <stdio.h>
//library to get random number
#include <stdlib.h>
//Library to calculate time
#include <time.h>

//Method to swap using a temp variable
int SwapUsingTemp()
{
    //initilize counter  
    int counter = 0;
    
    //loop 1000 times
    for(int i=0;i<1000;i++)
    {
      //Get random value for x and y
      int x = rand()%1000;
      int y = rand()%1000;
      int temp;
      
      //Print values of x and y before swap
      printf("Before swaping: x = %d and y = %d",x,y);
      printf("\n");
      
      //Swap using temp variable
      temp = x;
      x = y;
      y = temp;
      counter += 1;
      
      //print values of x and y after swaping
      printf("After swaping: x = %d and y = %d",x,y);
      printf("\n");
      printf("\n");
      
      
    }
    
    //print how many times the loop has run
    printf("This loop has run %d times", counter);
    
    
}



int main()

{
    // To calculate how long the program took
    clock_t t;
    t = clock();
    SwapUsingTemp();
    t = clock() - t; 
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("\n");
    printf("This program took %f seconds to execute \n", time_taken);
  
  
}