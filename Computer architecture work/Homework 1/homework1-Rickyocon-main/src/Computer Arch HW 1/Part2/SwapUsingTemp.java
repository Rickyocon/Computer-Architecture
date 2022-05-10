// Java program to swap two variables
// Using a Temp variable

public class SwapUsingTemp 
{

	public static void main(String[] args)
	{    
     
        //Start timer
        long StartTime = System.nanoTime(); 
    
        //initilize counter
        int counter = 0;

        //loop 1000 times
        for(int i = 1;i<=1000;i++)
        {
            //Get random value for x and y
            double x = (Math.random()*1000);
            double y = (Math.random()*1000);

            //Print values of x and y before swap
            System.out.println("Before Swap");
		    System.out.println("x = " + x);
		    System.out.println("y = " + y);

            //swap using temp variable
		    double temp = x;
		    x = y;
		    y = temp;
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



