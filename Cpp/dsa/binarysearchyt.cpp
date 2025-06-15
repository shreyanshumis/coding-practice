#include <iostream>
using namespace std;

int binarySearch(int arr[], int size, int key) {
    int start = 0;
    int end = size-1;
    int mid = (start+end)/2;

    while(start <= end)
    {
        if(arr[mid]==key){
            return mid;
        }

        if(key> arr[mid]){
            start = mid+1;
        }
        else{
            end = mid - 1;
        }
        mid = (start+end)/2;
    }
    return -1;
}



int main(){
    
    int even[6] = {1,4,6,8,10,15};
    int odd[5] = {2,3,5,6,8};

    int Evenindex = binarySearch(even,6,12);
    int Oddindex = binarySearch(odd,5,5);

    cout<<"Even index is "<< Evenindex<<endl;
    cout<<"Odd index is "<< Oddindex<<endl;
    return 0;
}