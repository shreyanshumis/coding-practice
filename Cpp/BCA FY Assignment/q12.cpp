#include <iostream>
using namespace std;
#define MAX_SIZE 5
class Stack {
private:
    int arr[MAX_SIZE];
    int top;
public:
    Stack() {
        top = -1;
    }
    bool isEmpty() {
        return (top == -1);
    }
    bool isFull() {
        return (top == MAX_SIZE - 1);
    }
    void push(int value) {
        if (isFull()) {
            cout << "Stack Overflow: Cannot push element " << value << ". Stack is full." << endl;
            return;
        }
        top++;
        arr[top] = value;
        cout << "Pushed element " << value << " into the stack." << endl;
    }
    void pop() {
        if (isEmpty()) {
            cout << "Stack Underflow: Cannot pop element. Stack is empty." << endl;
            return;
        }
        int poppedElement = arr[top];
        top--;
        cout << "Popped element " << poppedElement << " from the stack." << endl;
    }
    void display() {
        if (isEmpty()) {
            cout << "Stack is empty." << endl;
            return;
        }
        cout << "Stack elements: ";
        for (int i = top; i >= 0; i--) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};
int main() {
    Stack stack;
    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.push(40);
    stack.push(50);
    stack.push(60);
    stack.display();
    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();
    stack.display();
    return 0;
}
