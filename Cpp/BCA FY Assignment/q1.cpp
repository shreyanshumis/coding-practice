#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

vector<int> removeDuplicates(const vector<int>& arr) {
    unordered_set<int> uniqueElements;
    vector<int> result;
    for (int num : arr) {
        if (uniqueElements.find(num) == uniqueElements.end()) {
            uniqueElements.insert(num);
            result.push_back(num);
        }
    }
    return result;
}

int main() {
    vector<int> arr = {2, 4, 6, 8, 4, 10, 2, 6};
    vector<int> result = removeDuplicates(arr);
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
