#include <iostream>
#include <vector>
using namespace std;
void insertionSort(vector<int>& arr) {
    int n = arr.size();

    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}
int linearSearch(const vector<int>& arr, int target) {
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

int main() {
    vector<int> arr = {4, 2, 7, 1, 5, 9};
    insertionSort(arr);
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    int target = 5;
    int index = linearSearch(arr, target);
    if (index != -1) {
        cout << "Element found at index: " << index << endl;
    } else {
        cout << "Element not found" << endl;
    }
    return 0;
}

