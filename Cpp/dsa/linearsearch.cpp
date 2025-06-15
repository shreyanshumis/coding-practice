#include<iostream>
using namespace std;

bool search(int arr[], int size, int key)
{
    for(int i=0; i<size ;i++)
    {
        if(arr[i] == key)
        {
            return 1;
        }
    }
    return 0;
}

int main()
{
    int arr[10]={1,2,2003,69,11,420,98,-5,-96};
    cout <<"Enter the element to search for " << endl;
    int key;
    cin >> key;
    bool found = search(arr, 10, key);
    if(found)
    {
        cout<<"Value Present"<<endl;
    }
    else
    {
        cout<<"Value Absent"<<endl;
    }
}