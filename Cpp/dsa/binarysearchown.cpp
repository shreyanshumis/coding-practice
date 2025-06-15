#include <iostream>
#include<array>
using namespace std;

int main(){
    int arr[7] = {1,40,69,72,300,420,6942}; //assuming this is a sorted array.
    int startIndx = 0;
    int endIndx = sizeof(arr)/sizeof(arr[0]);
    int mid = (startIndx+endIndx)/2;
    int inpUser;
    cout<<"Enter a number to search"<<endl;
    cin>>inpUser;
    while (startIndx<=endIndx)
    {
        if(arr[mid]==inpUser)
        {
            cout<<"Element found!";
            break;
        }
        if (arr[mid]>inpUser){
            endIndx = mid;
        }
        else if (arr[mid]<inpUser)
        {
            startIndx = mid+1;
        }
        else
        {
            cout<<"Element not found >:(";
        }
        mid = (startIndx+endIndx)/2;
    }
    return 0;
}