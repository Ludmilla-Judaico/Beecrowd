#include <bits/stdc++.h>
using namespace std;

int main() 
{
    long long x, y, z;
    bool pit = false;
    while(cin >> x>>y>>z){
      if(x > y && x > z){
        if(x*x == y*y + z*z) pit = true;
      }else if(y > x && y > z){
        if(y*y == x*x + z*z) pit = true;
      }else{
        if(z*z == x*x + y*y) pit = true;
      }
      
      if(pit){
        long long mdc = gcd(gcd(x,y),z);
        if(mdc == 1) cout << "tripla pitagorica primitiva\n";
        else cout << "tripla pitagorica\n";
      }else{
        cout << "tripla\n";
      }
      pit = false;
    }
    return 0;
}
