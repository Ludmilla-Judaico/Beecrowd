#include <bits/stdc++.h>
using namespace std;

int main() 
{
  unsigned long long num;
  while(cin >> num && num != 0){
    string r="";
    unsigned long long resto;
    while(num != 0){
      resto = num%32;
      num = num/32;
      if(resto >= 10 && resto <= 31){
        unsigned long long s=resto+55;
        r = static_cast<char>(s) + r;
      }else{
        r = string(1, resto + '0') + r;
      }
    }
    cout << r << endl;
  }
  cout << 0 << endl;
  return 0;
}
