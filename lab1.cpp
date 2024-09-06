#include <iostream>
#include <stack>
using namespace std;

// Function prototypes
void show(stack<int> s);

// Main function
int main() {

    // Create a stack
    stack<int> s1;

    // Push elements to the stack
    s1.push(1);
    s1.push(2);
    s1.push(3);
    s1.push(4);

    // Show the stack
    cout << "Stack contents before popping:\n";
    show(s1);
    cout << endl;

    // Remove a few elements
    s1.pop();
    s1.pop();

    // Show the stack again
    cout << "Stack contents after popping:\n";
    show(s1);
    cout << endl;

    // Success!
    return 0;
}

// Show the stack using recursion
void show(stack<int> s) {
    if (s.empty()) {
        return;
    }
    
    // Print the top element
    cout << s.top() << " ";

    // Remove the top element
    s.pop();

    // Recursively call show to display the rest
    show(s);
}
