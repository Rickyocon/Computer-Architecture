// Java program to swap two variables
// Using XOR
import java.util.Random;

public class SwapXOR
{

	public static void main(String[] args)
	{    
     
        //start timer
        long StartTime = System.nanoTime();
        //initilize new random
        Random rand = new Random(); 
    
        //initlize counter
        int counter = 0;
        //set upper bound
        int upperbound = 1001;

        //loop 1000 times
        for(int i = 1;i<=1000;i++)
        {
            //Get random value for x and y
            int x = rand.nextInt(upperbound);
            int y = rand.nextInt(upperbound);

            //Print values of x and y before swap
            System.out.println("Before Swap");
		    System.out.println("x = " + x);
		    System.out.println("y = " + y);
            
            //Swap using XOR
            x = x ^ y; 
            y = x ^ y; 
            x = x ^ y;
            counter += 1;

            //print values of x and y after swaping
		    System.out.println("After swap");
		    System.out.println("x = " + x);
		    System.out.println("y = " + y);
            //print how many times the loop has run
            System.out.println("The loop has run " +counter +" times");

        }

        //end timer and calculate elapsed time
        long duration = (System.nanoTime() - StartTime)/1000000;  //Calculates time in mili seconds
        //print duration
        System.out.println("The program took " +duration + " ms");

	}
}

