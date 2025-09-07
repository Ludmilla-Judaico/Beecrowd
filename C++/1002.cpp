#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double circulo(double r){
    double pi = 3.14159;
    double area = pi * (pow(r,2));
    return area;
}

int main(){
    double r;
    cin >> r;
    cout << fixed << setprecision(4) << "A=" << circulo(r) << endl;
    return 0;
}