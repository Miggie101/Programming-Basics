#include <iostream>
#include <math.h>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    int fNumber, sNumber;

    cout << "This Program will let you enter two integer values that show you all the possible answers.\n";
    cout << "Please enter ONLY whole numbers!!\n";

    cout << "\nPlease enter your first whole number: ";
    cin >> fNumber;
    cout << "Please enter your second whole number : ";
    cin >> sNumber;

    int addAnswer = fNumber + sNumber;
    int subAnswer = fNumber - sNumber;
    int multiAnswer = fNumber * sNumber;
    float divAnswer = float(fNumber) / float(sNumber);
    int truncAnswer = trunc(divAnswer);
    int modAnswer = fNumber % sNumber;
    double expoAnswer = pow(fNumber, sNumber);
    
    cout << "\n" << fNumber << "+" << sNumber << "=" << addAnswer;
    cout << "\n" << fNumber << "-" << sNumber << "=" << subAnswer;
    cout << "\n" << fNumber << "*" << sNumber << "=" << multiAnswer;
    cout << "\n" << fNumber << "/" << sNumber << "=" << setprecision(2) << fixed << divAnswer;
    cout << "\n" << fNumber << "//" << sNumber << "=" << truncAnswer;
    cout << "\n" << fNumber << "%" << sNumber << "=" << modAnswer;
    cout << "\n" << fNumber << "**" << sNumber << "=" << setprecision(0) << fixed << expoAnswer;

    cout << "\n\nHave a great day :)!!!\n";

    return 0;
