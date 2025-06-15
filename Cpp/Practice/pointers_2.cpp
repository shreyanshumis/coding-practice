//Video was by Low Level learning on youtube on pointers
//link here - https://youtu.be/2ybLD6_2gKM


#include<iostream>
using namespace std;

int main()
{
    int x = 4;//Integer named x is set to 4
    int * pX = &x; //integer pointer(*) named px is set to the address of(&) x
    // the '*' here modifies the type . our var is now a pointer to an integer
    int y = *pX;//Integer named y is set to the thing pointed to by px
    //the '*' here is used for dereferencing. goes to the address, point it to by the pointer and get it's value. 
    cout<<y;//print and see if this works.
    return 0;
}