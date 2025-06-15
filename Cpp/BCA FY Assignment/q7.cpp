#include <iostream>
#include <vector>
using namespace std;
void insertElement(vector<int>& arr, int newElement) {
    int n = arr.size();
    int i = n - 1;
    while (i >= 0 && arr[i] > newElement) {
        arr[i + 1] = arr[i];
        i--;
    }
    arr[i + 1] = newElement;
}

int main() {
    vector<int> arr = {2, 4, 7, 9, 11};
    int newElement = 6;

    cout << "Original Array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    insertElement(arr, newElement);
    cout << "Updated Array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
