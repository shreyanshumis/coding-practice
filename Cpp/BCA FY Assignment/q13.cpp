#include <iostream>
using namespace std;
#define MAX_SIZE 5
class Queue {
private:
    int arr[MAX_SIZE];
    int front, rear;
public:
    Queue() {
        front = -1;
        rear = -1;
    }
    bool isEmpty() {
        return (front == -1 && rear == -1);
    }
    bool isFull() {
        return (rear == MAX_SIZE - 1);
    }
    void enqueue(int value) {
        if (isFull()) {
            cout << "Queue Overflow: Cannot enqueue element " << value << ". Queue is full." << endl;
            return;
        }
        if (isEmpty()) {
            front = 0;
            rear = 0;
        } else {
            rear++;
        }
        arr[rear] = value;
        cout << "Enqueued element " << value << " into the queue." << endl;
    }
    void dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow: Cannot dequeue element. Queue is empty." << endl;
            return;
        }
        int dequeuedElement = arr[front];

        if (front == rear) {
            // If the queue has only one element
            front = -1;
            rear = -1;
        } else {
            front++;
        }
        cout << "Dequeued element " << dequeuedElement << " from the queue." << endl;
    }
    void display() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return;
        }
        cout << "Queue elements: ";
        for (int i = front; i <= rear; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};
int main() {
    Queue queue;
    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);
    queue.enqueue(40);
    queue.enqueue(50);
    queue.enqueue(60);
    queue.display();
    queue.dequeue();
    queue.dequeue();
    queue.dequeue();
    queue.display();
    return 0;
}