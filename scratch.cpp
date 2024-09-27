#include <iostream>;
using namespace std;

int main() {
   int sumX = 0;
   int sumY = 0;
   do {
      sumX++;
      sumY++;
      sumX += sumY;
   } while (sumX < 2);

   cout << "sumX: " << sumX << " sumY: " << sumY;
   return 0;
}