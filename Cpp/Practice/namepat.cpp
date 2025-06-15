#include <iostream>
using namespace std;

int pat()
{
    cout<<"Enter your name"<<endl;
    string name;
    cin>>name;
    int nameleng = name.length();
    for(int i=0; i<nameleng;i++)
    {
        for(int j=0; j<i;j++)
        {
            cout<<name[j];
        }
        cout<<"\n";
    }
    for(int k=nameleng; k>=0;k--)
    {
        for(int l=0; l<k; l++)
        {
            cout<<name[l];
        }
        cout<<"\n";
    }
}

int main()
{
    pat();
    return 0;
}