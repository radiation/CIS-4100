#include <iostream>
#include <queue>
using namespace std;

// Function prototypes
void show(queue<int> s);

// Main function
int main() {

    // Create a queue
    queue<int> q1;

    // Push elements to the queue
    q1.push(1);
    q1.push(2);
    q1.push(3);
    q1.push(4);

    // Show the queue
    cout << "Queue contents before popping:\n";
    show(q1);
    cout << endl;

    // Remove a few elements
    q1.pop();
    q1.pop();

    // Show the queue again
    cout << "Queue contents after popping:\n";
    show(q1);
    cout << endl;

    // Success!
    return 0;
}

// Show the queue using recursion
void show(queue<int> q) {
    if (q.empty()) {
        return;
    }
    
    // Print the top element
    cout << q.front() << " ";

    // Remove the top element
    q.pop();

    // Recursively call show to display the rest
    show(q);
}
