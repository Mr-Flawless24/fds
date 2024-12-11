#include <iostream>
#include <stdlib.h>
using namespace std;

class node {
public:
    node* next;
    node* prev;
    int seat;
    string id;
    int status;  // 0 = available, 1 = booked
};

class Cinemax {
public:
    node* head, * tail, * temp;
    Cinemax() {
        head = NULL;
    }
    void create_list();
    void display();
    void book();
    void cancel();
    void avail();
};

void Cinemax::create_list() {
    temp = new node;
    temp->seat = 1;
    temp->status = 0;
    temp->id = "null";
    tail = head = temp;

    for (int i = 2; i <= 70; i++) {
        node* p = new node;
        p->seat = i;
        p->status = 0;
        p->id = "null";
        tail->next = p;
        p->prev = tail;
        tail = p;
    }

    tail->next = head;
    head->prev = tail;
}

void Cinemax::display() {
    node* temp = head;
    int count = 0;
    cout << "\n------------------------------------------------------------------------------------\n";
    cout << " Screen this way \n";
    cout << "------------------------------------------------------------------------------------\n";

    do {
        if (temp->seat < 10)
            cout << "S0" << temp->seat << " :";
        else
            cout << "S" << temp->seat << " :";

        if (temp->status == 0)
            cout << "|___| ";
        else
            cout << "|_B_| ";

        count++;
        if (count % 7 == 0)
            cout << endl;

        temp = temp->next;
    } while (temp != head);
}

void Cinemax::book() {
    int x;
    string y;

    while (true) {
        cout << "\n\nEnter seat number to be booked (eg. 33):\n";
        cin >> x;
        if (x < 1 || x > 70) {
            cout << "Enter correct seat number \n";
            continue;
        }
        break;
    }

    cout << "Enter your ID number(eg. S33):\n";
    cin >> y;

    node* temp = head;
    while (temp->seat != x) {
        temp = temp->next;
    }

    if (temp->status == 1)
        cout << "Seat already booked!\n";
    else {
        temp->status = 1;
        temp->id = y;
        cout << "Seat " << x << " booked!\n";
    }
}

void Cinemax::cancel() {
    int x;
    string y;

    while (true) {
        cout << "Enter seat number to cancel booking (1-70):\n";
        cin >> x;
        if (x < 1 || x > 70) {
            cout << "Enter correct seat number (1-70)\n";
            continue;
        }
        break;
    }

    cout << "Enter your ID:\n";
    cin >> y;

    node* temp = head;
    while (temp->seat != x) {
        temp = temp->next;
    }

    if (temp->status == 0) {
        cout << "Seat not booked yet!\n";
    } else {
        if (temp->id == y) {
            temp->status = 0;
            cout << "Seat cancelled!\n";
        } else {
            cout << "Wrong User ID! Seat cannot be cancelled.\n";
        }
    }
}

void Cinemax::avail() {
    node* temp = head;
    int count = 0;

    cout << "\n------------------------------------------------------------------------------------\n";
    cout << " Available Seats \n";
    cout << "------------------------------------------------------------------------------------\n";

    do {
        if (temp->seat < 10)
            cout << "S0" << temp->seat << " :";
        else
            cout << "S" << temp->seat << " :";

        if (temp->status == 0)
            cout << "|___| "; // Available
        else
            cout << "     "; // Empty space for booked seats

        count++;
        if (count % 7 == 0)
            cout << endl;

        temp = temp->next;
    } while (temp != head);
}

int main() {
    Cinemax obj;
    obj.create_list();

    int ch;
    char c = 'y';
    while (c == 'y') {
        obj.display();
        cout << "\n*********************************************\n";
        cout << " CINEMAX MOVIE THEATRE\n";
        cout << "*********************************************\n";
        cout << "\nEnter Choice\n1.Current SeatStatus\n2.Book Seat \n3.Available Seat\n4.Cancel Seat\n";
        cin >> ch;

        switch (ch) {
            case 1:
                obj.display();
                break;
            case 2:
                obj.book();
                break;
            case 3:
                obj.avail();
                break;
            case 4:
                obj.cancel();
                break;
            default:
                cout << "Wrong choice input\n";
        }

        cout << "\nDo you want to perform any other operation? (y/n)\n";
        cin >> c;
    }

    return 0;
}
