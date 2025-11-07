#include <bits/stdc++.h>
using namespace std;

int main() 
{
    long long num; 
    while(cin >> num)
    {
      long long divisor=0;
      long long tam=0;
      for(long long i=0 ; i<=num ; i++){
        divisor = (divisor * 10 + 1) % num;
        tam +=1;
        if(divisor == 0) break;
      }
      
      cout << tam << '\n';
    }

    return 0;
}
