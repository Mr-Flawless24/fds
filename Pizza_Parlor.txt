#include <iostream>
using namespace std;

class PizzaParlor {
    int front, rear, size;
    int* queue;

public:
    PizzaParlor(int M) {
        size = M;
        front = rear = -1;
        queue = new int[size];
    }

    bool isFull() {
        return (rear + 1) % size == front;
    }

    bool isEmpty() {
        return front == -1;
    }

    void placeOrder(int orderNumber) {
        if (isFull()) {
            cout << "Pizza parlor is full! Cannot accept more orders." << endl;
            return;
        }
        if (front == -1) {
            front = 0;
        }
        rear = (rear + 1) % size;
        queue[rear] = orderNumber;
        cout << "Order " << orderNumber << " placed successfully." << endl;
    }

    void serveOrder() {
        if (isEmpty()) {
            cout << "No orders to serve!" << endl;
            return;
        }
        cout << "Serving order " << queue[front] << endl;
        if (front == rear) {
            front = rear = -1;
        } else {
            front = (front + 1) % size;
        }
    }

    void displayOrders() {
        if (isEmpty()) {
            cout << "No orders to display!" << endl;
            return;
        }
        cout << "Orders in the queue: ";
        int i = front;
        while (true) {
            cout << queue[i] << " ";
            if (i == rear) break;
            i = (i + 1) % size;
        }
        cout << endl;
    }
};

int main() {
    int M;
    cout << "Enter the maximum number of orders the pizza parlor can accept: ";
    cin >> M;

    PizzaParlor parlor(M);

    parlor.placeOrder(101);
    parlor.placeOrder(102);
    parlor.placeOrder(103);
    parlor.displayOrders();

    parlor.serveOrder();
    parlor.displayOrders();

    parlor.placeOrder(104);
    parlor.placeOrder(105);
    parlor.displayOrders();

    return 0;
}
