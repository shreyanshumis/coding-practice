#include <iostream>
using namespace std;

int arr()
{
    int n;
    cout<<"Enter 4 laptop names";
    cin>>n;
    string laptops[n] = {};
    for(int i=0; i<4; i++)
    {
        cout << laptops[i] << endl;
    }
}

int main()
{
    arr();
    return 0;
}