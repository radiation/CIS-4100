// clock.h

#ifndef CLOCK_H
#define CLOCK_H

#include <string>
using namespace std;

class Clock {

    private:
        int hours;
        int minutes;
        int seconds;
        string meridian; // "AM" or "PM"

    public:
        // Constructor
        Clock(int h = 12, int m = 0, int s = 0, const string& mer = "AM");

        // Setters
        void setHours(int h);
        void setMinutes(int m);
        void setSeconds(int s);
        void setMeridian(const string& mer);

        // Getters
        int getHours() const;
        int getMinutes() const;
        int getSeconds() const;
        string getMeridian() const;

        // Methods to display the time
        void displayStandard() const;
        void displayMilitary() const;

        // Method to add seconds and adjust time
        void addSeconds(int s);

};

#endif