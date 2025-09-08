#include <iostream>
#include <climits>
using namespace std;

int main()
{
    int a = 7;
    int b = 3;

    cout << "a = " << a << ", b = " << b << endl;
    cout << &a << " " << &b << endl;

    int n_int = INT_MAX;
    long long n_llong = LLONG_MAX;

    cout << "int " << sizeof n_int << "byte, max is " << n_int << endl;
    cout << "long long " << sizeof n_llong << "byte, max is " << n_llong << endl;

    unsigned int c = -1;
    cout << c << endl;

    float d = 3.14;
    int e = 3.14;

    cout << d << " " << e << endl;

    return 0;
}