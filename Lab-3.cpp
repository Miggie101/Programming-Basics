#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int base;
	int exponent;

   cout << "This program will let the user raise any integer to any power\n";
   cout << "Hello user. Welcome to the Power Caculator!\n";
   cout << "Remeber to use WHOLE numbers\n";

   cout << "\nPlease enter the base number: ";
   cin >> base;

   cout << "Please enter the power number for " << base << ": ";
   cin >> exponent;

   double answer = pow(base, exponent);

   cout << "\n" << base << " raised to the power of " << exponent << " equals " << int(answer) << "\n";

   cout << "\nHave a nice day!! :)\n";

   return 0;
}
