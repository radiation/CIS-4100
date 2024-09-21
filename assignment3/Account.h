// Account.h

#ifndef ACCOUNT_H
#define ACCOUNT_H

class Account {
private:
    double balance;         // To store the account balance
    double interestRate;    // To store the interest rate

public:
    // Constructor
    Account(double initialBalance = 0.0);

    // Setters
    void setInterestRate(double rate);

    // Getters
    double getBalance() const;
    double getInterestRate() const;

    // Method to make a deposit
    void makeDeposit(double amount);

    // Method to calculate interest
    double calculateInterest() const;

    // Method to check if withdrawal is possible
    bool canWithdraw(double amount) const;

    // Method to withdraw
    bool makeWithdrawal(double amount);
};

#endif // ACCOUNT_H

