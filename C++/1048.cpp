#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    float salario_a, salario_n, porc;
    salario_n = 0;

    cin >> salario_a;

    if(salario_a > 0 && salario_a <= 400.00){
        porc = 1.15;
        salario_n = salario_a * porc;

    }else if(salario_a >= 400.01 && salario_a <= 800.00){
        porc = 1.12;
        salario_n = salario_a * porc;

    }else if(salario_a >= 800.01 && salario_a <= 1200.00){
        porc = 1.10;
        salario_n = salario_a * porc;

    }else if(salario_a >= 1200.01 && salario_a <= 2000.00){
        porc = 1.07;
        salario_n = salario_a * porc;

    }else if(salario_a > 2000){
        porc = 1.04;
        salario_n = salario_a * porc;
    }

    cout << "Novo salario: " << fixed << setprecision(2) << salario_n << endl;
    cout << "Reajuste ganho: " << salario_n - salario_a << endl;
    cout << "Em percentual: " << fixed << setprecision(0) << (porc * 100) - 100 << " %" << endl;
    return 0;
}