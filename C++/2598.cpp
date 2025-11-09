#include <bits/stdc++.h>
using namespace std;

int main() 
{
    long long t; cin >> t;
    double av, area;
    for(long long i=0 ; i<t ; i++){
      cin >> av>>area;
      double r = ceil(av/area);
      cout << r << '\n';
    }
    return 0;
}
