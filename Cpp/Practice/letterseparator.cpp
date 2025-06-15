#include <iostream>
using namespace std;

int separator()
{
    cout<<"Enter your name"<<endl;
    string name;
    cin>>name;
    int nameleng = name.length();
    for(int i=0; i<nameleng; i++)
    {   
        char ltrname=name[i];
        cout<<ltrname<<endl;
    }
}
int main()
{
    separator();
    return 0;
}