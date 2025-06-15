#include <iostream>
using namespace std;
#define MAX_SIZE 5
class CircularQueue {
private:
    int arr[MAX_SIZE];
    int front, rear;
public:
    CircularQueue() {
        front = -1;
        rear = -1;
    }
    bool isEmpty() {
        return (front == -1 && rear == -1);
    }
    bool isFull() {
        if ((rear + 1) % MAX_SIZE == front)
            return true;
        return false;
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
            rear = (rear + 1) % MAX_SIZE;
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
            front = -1;
            rear = -1;
        } else {
            front = (front + 1) % MAX_SIZE;
        }
        cout << "Dequeued element " << dequeuedElement << " from the queue." << endl;
    }
    void display() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return;
        }
        cout << "Queue elements: ";
        int i = front;
        while (i != rear) {
            cout << arr[i] << " ";
            i = (i + 1) % MAX_SIZE;
        }
        cout << arr[rear] << endl;
    }
};
int main() {
    CircularQueue queue;
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
