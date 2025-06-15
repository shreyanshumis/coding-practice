#include <iostream>
using namespace std;

int SwapPointers(int* a, int* b) //Pointers
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int SwapRefvar(int &a, int &b)  //Reference Variables
{
    int temp = a;
    a = b;
    b = temp;
}

int main(){
    int x, y;
    cout<<"Enter two numbers to swap"<<endl;
    cin>>x>>y;
    cout<<"\n";
    cout<<"The value of A is "<<x<<" and the value of b is "<<y<<endl;
    SwapPointers(&x, &y);
    cout<<"x and y are : "<<x<<","<<y<<endl;
    SwapRefvar(x, y);
    cout<<"x and y are : "<<x<<","<<y<<endl;
    return 0;
}