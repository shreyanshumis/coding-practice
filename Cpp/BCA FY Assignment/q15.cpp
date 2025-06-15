#include <iostream>
#define MAX_SIZE 10
using namespace std;
class LinearList {
private:
    int arr[MAX_SIZE];
    int length;
public:
    LinearList() {
        length = 0;
    }

    bool isEmpty() {
        return (length == 0);
    }

    bool isFull() {
        return (length == MAX_SIZE);
    }
    void display() {
        if (isEmpty()) {
            cout << "Linear List is empty." << endl;
            return;
        }
        cout << "Linear List elements: ";
        for (int i = 0; i < length; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
    void insert(int value, int position) {
        if (isFull()) {
            cout << "Linear List Overflow: Cannot insert element " << value << ". Linear List is full." << endl;
            return;
        }
        if (position < 0 || position > length) {
            cout << "Invalid position. Cannot insert element." << endl;
            return;
        }
        for (int i = length - 1; i >= position; i--) {
            arr[i + 1] = arr[i];
        }
        arr[position] = value;
        length++;
        cout << "Inserted element " << value << " at position " << position << "." << endl;
    }
    void remove(int position) {
        if (isEmpty()) {
            cout << "Linear List Underflow: Cannot remove element. Linear List is empty." << endl;
            return;
        }
        if (position < 0 || position >= length) {
            cout << "Invalid position. Cannot remove element." << endl;
            return;
        }
        int removedElement = arr[position];
        for (int i = position; i < length - 1; i++) {
            arr[i] = arr[i + 1];
        }
        length--;
        cout << "Removed element " << removedElement << " from position " << position << "." << endl;
    }
    int search(int value) {
        if (isEmpty()) {
            cout << "Linear List is empty. Cannot search for element." << endl;
            return -1;
        }

        for (int i = 0; i < length; i++) {
            if (arr[i] == value) {
                return i;
            }
        }
        return -1;
    }
};
int main() {
    LinearList list;
    list.display();
    list.insert(10, 0);
    list.insert(20, 1);
    list.insert(30, 2);
    list.insert(40, 3);
    list.insert(50, 2);
    list.display();
    list.remove(3);
    list.display();
    int searchValue = 30;
    int position = list.search(searchValue);
    if (position != -1) {
        cout << "Element " << searchValue << " found at position " << position << "." << endl;
    } else {
        cout << "Element " << searchValue << " not found." << endl;
    }
    return 0;
}
