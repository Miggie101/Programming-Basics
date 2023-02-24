#include <iostream>

using namespace std;

int main()
{
    string lastName; 
    string name; 

    cout << "This program will ask for the users first and last name and display a message.\n";
    cout << "Hello user, please follow these intructions.\n";
    cout << "Please enter your name: ";
    cin >> name;
    cout << "Please enter youir last name: ";
    cin >> lastName;
    cout << "\n";
    cout << "Hello " + name + " " + lastName;
    cout << "\nWelcome to C++\n";
    cout << "Thank you, have a nice dia!!"; 

    return 0; 
