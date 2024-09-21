// main.cpp

#include <iostream>
#include "Account.h"
using namespace std;

int main() {

    // Create an Account object with an initial balance of 1000
    Account myAccount(1000.0);

    // Set the interest rate
    myAccount.setInterestRate(0.05);

    // Make a deposit
    myAccount.makeDeposit(500.0);

    // Display the current balance
    cout << "Current Balance: $" << myAccount.getBalance() << endl;

    // Calculate and display the interest
    double interest = myAccount.calculateInterest();
    cout << "Interest: $" << interest << endl;

    // Try to withdraw an amount
    double withdrawalAmount = 700.0;
    if (myAccount.makeWithdrawal(withdrawalAmount)) {
        cout << "Successfully withdrew: $" << withdrawalAmount << endl;
    } else {
        cout << "Failed to withdraw: $" << withdrawalAmount << endl;
    }

    // Display the final balance
    cout << "Final Balance: $" << myAccount.getBalance() << endl;
    cout << "Interest after one year: $" << myAccount.calculateInterest() << endl;
    cout << "Total balance after one year: $" << myAccount.getBalance() + myAccount.calculateInterest() << endl;

    return 0;

}