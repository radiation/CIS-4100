#include <iostream>
using namespace std;

// Function prototypes
void readInputs(double &price, double &quantity);

// This is immutable so we'll set it globally
const double NY_SALES_TAX = 0.0875;

int main() {
    double price, quantity, subtotal, taxes, total;

    // Passed by reference
    readInputs(price, quantity);

    // Do math
    subtotal = price * quantity;
    taxes = subtotal * NY_SALES_TAX;
    total = subtotal + taxes;

    // Output
    cout << "Subtotal: $" << subtotal << endl;
    cout << "Taxes: $" << taxes << endl;
    cout << "Total: $" << total << endl;

    // Success
    return 0;
}

// Read inputs and return to the main program
void readInputs(double &price, double &quantity) {
    cout << "Enter the price of an item: ";
    cin >> price;

    while (price <= 0) {
        cout << "Price must be a positive value. Please enter a different value: ";
        cin >> price;
    }

    cout << "Enter the quantity: ";
    cin >> quantity;

    while (quantity <= 0) {
        cout << "Quantity must be a positive value. Please enter a different value: ";
        cin >> quantity;
    }
}