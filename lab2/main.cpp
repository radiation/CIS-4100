// main.cpp
#include <iostream>
#include "clock.h"  // Include the header file

int main() {
    // Create a Clock object
    Clock myClock(11, 59, 50, "AM");

    // Display the time
    myClock.displayStandard();
    myClock.displayMilitary();

    // Add 20 seconds & display the time
    myClock.addSeconds(20);
    myClock.displayStandard();
    myClock.displayMilitary();

    // Set the time to 5:00 PM & display the time
    myClock.setHours(5);
    myClock.setMeridian("PM");
    myClock.displayStandard();
    myClock.displayMilitary();

    return 0;
}
