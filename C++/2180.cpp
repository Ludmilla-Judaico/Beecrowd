#include <bits/stdc++.h>
using namespace std;
bool primo(long long num){
  if(num == 1) return false;
  if(num == 2) return true;
  if(num%2 == 0) return false;
  for(long long i=3 ; i*i<num ; i+=2){
    if(num%i == 0) return false;
  }
  return true;
}

int main() 
{
    long long peso, soma=0; cin >> peso;
    long long ini=peso;
    for(long long i=0 ; i<10 ; i++){
      while(!(primo(ini))){
       ini++;
      }
      soma+=ini;
      ini++;
    }
    long long h=60000000/soma;
    long long d=h/24;
    cout << soma << " km/h\n";
    cout << h << " h / " << d << " d\n";
    
    return 0;
}
