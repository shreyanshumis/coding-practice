/*Notes needed for an amount
Eg: 1330
500 - ??
100- ??
50- ??
20- ??
10- ??      */

#include <iostream>
using namespace std;

int main(){
    int moneh,count,n;
    cout<<"Enter the amount"<<endl;
    cin>>moneh;

    if(moneh>500)
    {
        n=moneh/500;
        cout<<"The amount of 500 rs. notes is:"<<n<<endl;
        moneh=moneh%500;

    if(moneh>=100)
    {
        n = moneh/100;
        cout<<"The amount of 100 rs. notes is:"<<n<<endl;
        moneh=moneh%100;
    }

    if(moneh>=50)
    {
        n = moneh/50;
        cout<<"The amount of 50 rs. notes is:"<<n<<endl;
        moneh=moneh%50;
    }
    if(moneh>=20)
    {
        n = moneh/20;
        cout<<"The amount of 20 rs. notes is:"<<n<<endl;
        moneh=moneh%20;
    }
    if(moneh>=10)
    {
        n = moneh/10;
        cout<<"The amount of 10 rs. notes is:"<<n<<endl;
        moneh=moneh%10;
    }
}
