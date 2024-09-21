// clock.cpp

#include "clock.h"
#include <iostream>
#include <iomanip>
using namespace std;

// Constructor implementation
Clock::Clock(int h, int m, int s, const string& mer) : hours(h), minutes(m), seconds(s), meridian(mer) {}

// Setters
void Clock::setHours(int h) {
    if (h >= 1 && h <= 12) {
        hours = h;
    }
}

void Clock::setMinutes(int m) {
    if (m >= 0 && m < 60) {
        minutes = m;
    }
}

void Clock::setSeconds(int s) {
    if (s >= 0 && s < 60) {
        seconds = s;
    }
}

void Clock::setMeridian(const string& mer) {
    if (mer == "AM" || mer == "PM") {
        meridian = mer;
    }
}

// Getters
int Clock::getHours() const {
    return hours;
}

int Clock::getMinutes() const {
    return minutes;
}

int Clock::getSeconds() const {
    return seconds;
}

string Clock::getMeridian() const {
    return meridian;
}

// Methods to display the time
void Clock::displayStandard() const {
    cout << setw(2) << setfill('0') << hours << ":"
              << setw(2) << setfill('0') << minutes << ":"
              << setw(2) << setfill('0') << seconds << " "
              << meridian << endl;
}

void Clock::displayMilitary() const {
    int militaryHours;
    if (meridian == "PM") {
        militaryHours = hours + 12;
    }
    else {
        militaryHours = hours;
    }
    cout << setw(2) << setfill('0') << militaryHours << ":"
              << setw(2) << setfill('0') << minutes << ":"
              << setw(2) << setfill('0') << seconds << endl;
}

// Method to add seconds and adjust time accordingly
void Clock::addSeconds(int s) {
    seconds += s;
    if (seconds >= 60) {
        minutes += seconds / 60;
        seconds %= 60;
    }

    if (minutes >= 60) {
        hours += minutes / 60;
        minutes %= 60;
    }

    if (hours > 12) {
        hours %= 12;
        if (hours == 0) {
            hours = 12;
        }
        meridian = (meridian == "AM") ? "PM" : "AM";
    } else if (hours == 12) {
        meridian = (meridian == "AM") ? "PM" : "AM";
    }
}
