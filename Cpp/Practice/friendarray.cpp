#include <iostream>
using namespace std;

int arr()
{
    int i;
    cout<<"Enter the number of friends you have"<<endl;
    cin>>i;
    //-------------------------
    string friends[i]; //Not recommended
    //-------------------------
    cout<<"Enter the names of your friends"<<endl;
    for(int g=0;g<i;g++)
    {
        cin>>friends[g];
    }
    cout<<"Your friends are:"<<endl;
    for(int j=0;j<i;j++)
    {
        cout<<friends[j]<<endl;
    }
}
int main()
{
    arr();
    return 0;
}