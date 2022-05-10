//Method to swap two variables using a temp variable


#include <iostream>
//library for calculating program time
#include <ctime>
//library for getting a random number
#include <chrono>
using namespace std;


int main ()
{
    //Start timer
    auto StartTime = std::chrono::steady_clock::now();
    //initilize rand
    int rand();
    //initilize method for counter
    int counter = 0;

    //Loop for 1000 times
    for(int i=0;i<1000;i++)
    {
        //Get a random integer for x and y from 1-1000
        //initilize temp
        int temp;
        int x = rand()%1000;
        int y = rand()%1000;

        //print x and y values before swap
        cout << "\nBefore swapping." << endl;
        cout << "x = " << x << ", y = " << y << endl;

        //Mehtod to swap using temp variable
        temp = x;
        x = y;
        y = temp;
        counter += 1;

        //print x and y values after swap
        cout << "After swapping." << endl;
        cout << "x = " << x << ", y = " << y << endl;


    }

    //Print how many times the loop has run using counter variable
    cout << "The loop has run "<<counter<<" times"<<endl; 
    //End timer
    auto EndTime = std::chrono::steady_clock::now();
    //Calculate elapsed time by subtracting endtime and starttime in miliseconds
    double elapsed_time = double (std::chrono::duration_cast <std::chrono::milliseconds> (EndTime - StartTime).count());
    //print how long the program took
    cout <<"This program took "<<elapsed_time<<" ms"<<endl;
    return 0;

}