#include <bits/stdc++.h>
using namespace std;

bool primo(long long num){
  if(num == 1) return false;
  if(num == 2) return true;
  if(num % 2 == 0) return false;
  for(long long i=3 ; i*i<=num ; i+=2){
    if(num % i == 0) return false;
  }
  return true;
}

int main() 
{
  long long n;
  while(cin>>n){
    string str_n = to_string(n);
    bool super = true;
    if(primo(n)){
      for(long long i=0 ; i<str_n.size() ; i++){
        if(!primo(str_n[i] - '0')){
          super = false;
          break;
        }
      }
      if(super) cout << "Super\n";
      else cout << "Primo\n";
    }else{
      cout << "Nada\n";
    }
  }
    return 0;
}
