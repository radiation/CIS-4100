// Account.cpp

#include "Account.h"

// Constructor
Account::Account(double initialBalance) : balance(initialBalance), interestRate(0.0) {}

// Set the interest rate
void Account::setInterestRate(double rate) {
    if (rate >= 0) {
        interestRate = rate;
    }
}

// Get the account balance
double Account::getBalance() const {
    return balance;
}

// Get the interest rate
double Account::getInterestRate() const {
    return interestRate;
}

// Method to make a deposit
void Account::makeDeposit(double amount) {
    if (amount > 0) {
        balance += amount;
    }
}

// Method to calculate interest
double Account::calculateInterest() const {
    return balance * interestRate;
}

// Method to check if withdrawal is possible
bool Account::canWithdraw(double amount) const {
    return (amount > 0 && amount <= balance);
}

// Method to make a withdrawal
bool Account::makeWithdrawal(double amount) {
    if (canWithdraw(amount)) {
        balance -= amount;
        return true;
    }
    return false;
}

