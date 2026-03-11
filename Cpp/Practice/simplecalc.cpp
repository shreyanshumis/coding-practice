#include <iostream>
using namespace std;

double add(double x,double y){
    return x+y;
}
double sub(double x,double y){
    return x-y;
}
double mult(double x,double y){
    return x*y;
}
double div(double x,double y){
    return x/y;
}
double mod(double x,double y){
    return x+y;
}

int main() {
    double num1,num2, opt;
    cout<<"Enter two numbers:";
    cin>>num1>>num2;
    cout<<"Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for remainder.";
    cin>> opt;
    if (opt==1)
    {
        cout<<add(num1, num2);
    }
    else if (opt==2)
    {
        cout<<sub(num1, num2);
    }
    else if (opt==3)
    {
        cout<<mult(num1, num2);
    }
    else if (opt==4)
    {
        cout<<div(num1, num2);
    }
    else if (opt==5)
    {
        cout<<mod(num1, num2);
    }
    else
    {
    cout<<"Invalid input";
    }
    return 0;
}