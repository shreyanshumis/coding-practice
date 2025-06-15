#include<iostream>
using namespace std;
int c=45;
int main(){
    int a, b, c;
    cout<<"Enter the value of a:"<<endl;
    cin>>a;
    cout<<"Enter the value of b:"<<endl;
    cin>>b;
    c=a+b;
    cout<<"The sum is "<<c<<endl;
    cout<<"The global c is "<<::c;
 
    /* :: is a scope resolution operator
    you can use global variables inside a block 
    >=>=>=>=>=>=>=>=>=>=>=>=>
    The default floating point data type is double
    so you need to add f in the end of the number to show that it's float 
    and L in the end to show that it's a long double...
    
    float d=34.4F;
    long double e= 34.4L*/

    cout<<"The size of 34.4f is "<<sizeof(34.4f);

}