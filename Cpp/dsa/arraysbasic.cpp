#include <iostream>
using namespace std;

int main() {
    const int size = 5;
    int numbers[size];
    cout << "Enter " << size << " numbers:" << endl;
    for (int i = 0; i < size; ++i) {
        cout << "Number " << i + 1 << ": ";
        cin >> numbers[i];
    }

    cout << "Numbers entered:" << endl;
    for (int i = 0; i < size; ++i) {
        cout << numbers[i] << " ";
    }
    cout << endl;
    return 0;
}
