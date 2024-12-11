#include <iostream>
#include <cstring>
using namespace std;
#define MAX 50

class STACK {
private:
    char a[MAX];
    int top;

public:
    STACK() { top = -1; }

    void push(char c);
    void reverse();
    void convert(char str[]);
    void palindrome();
};

void STACK::push(char c) {
    if (top >= MAX - 1) {
        cout << "\nStack Overflow! Cannot push more characters.";
        return;
    }
    top++;
    a[top] = c;
    a[top + 1] = '\0';
    cout << c << " is pushed onto the Stack." << endl;
}

void STACK::reverse() {
    cout << "\nReversed String is: ";
    for (int i = top; i >= 0; i--) {
        cout << a[i];
    }
    cout << endl;
}

void STACK::convert(char str[]) {
    int k = 0;
    int len = strlen(str);
    for (int j = 0; j < len; j++) {
        if (isalpha(str[j])) { // Check if the character is alphabetic
            str[k] = tolower(str[j]); // Convert to lowercase
            k++;
        }
    }
    str[k] = '\0'; // Null-terminate the string
    cout << "\nConverted String: " << str << endl;
}

void STACK::palindrome() {
    char str[MAX];
    int j = 0;

    // Reverse the stack content into a new string
    for (int i = top; i >= 0; i--, j++) {
        str[j] = a[i];
    }
    str[j] = '\0'; // Null-terminate the reversed string

    // Compare the original stack content with the reversed string
    if (strcmp(str, a) == 0)
        cout << "\nString is a palindrome.";
    else
        cout << "\nString is not a palindrome.";
}

int main() {
    STACK stack;
    char str[MAX];

    cout << "\nEnter a String to check if it is a Palindrome or not:\n";
    cin.getline(str, MAX);

    stack.convert(str);

    for (int i = 0; str[i] != '\0'; i++) {
        stack.push(str[i]);
    }

    stack.palindrome();
    stack.reverse();

    return 0;
}
