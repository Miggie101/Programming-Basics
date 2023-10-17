#include <iostream>
using namespace std;
//is_odd() return true
//if n is odd, false otherwise
bool is_odd(int n){
  //check if n is odd
  if(n % 2 == 1){
    //n is odd
    return true;
  }
}

int main(){
  //declare necessary variables
  int start = 0, end = 0, sum = 0;
  do{
    cout << "Enter an startpoint";
    cin >> start;
    cout << "Enter an endpint";
  }while(start > end);
  for(int i = start + 1; i < end; i++){
    //send i to is_odd to determine if odd
    if(is_odd(i) == true){
      cout << i << "";
      sum+=i;
    }
  }
  cout << "The sum of those odd #'s is: " << sum << endl;
  return 0;
}
