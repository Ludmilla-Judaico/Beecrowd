#include <bits/stdc++.h>
using namespace std;

int main() 
{
    long long t; cin >> t;
    for(long long i=0 ; i<t ; i++){
      long long f1, f2; cin >> f1>>f2;
      cout << gcd(f1, f2) << '\n';
    }
    return 0;
}
