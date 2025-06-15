#include <iostream>
#include <vector>
using namespace std;
void deleteElement(vector<int>& arr, int target) {
    int n = arr.size();
    int i = 0;
    int j = 0;
    while (i < n && arr[i] != target) {
        i++;
    }
    if (i < n) {
        for (j = i; j < n - 1; j++) {
            arr[j] = arr[j + 1];
        }
    }
    arr.resize(n - 1);
}

int main() {
    vector<int> arr = {2, 4, 6, 7, 9, 11};
    int target = 6;
    cout << "Original Array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    deleteElement(arr, target);
    cout << "Updated Array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
