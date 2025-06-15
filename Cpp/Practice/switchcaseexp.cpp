#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter a number"<<"1 - Option 1 \n 2 - Option 2 \n 3- Option 3" << endl;
    cin>>n;
    switch (n)
    {
    case 1:
        cout<<"Option 1";
        break;
    case 2:
        cout<<"Option 2";
        break;
    case 3:
        cout<<"Option 3";
        break;
    default:
        cout<<"Akhi kharap ki?";
        break;
    }
}