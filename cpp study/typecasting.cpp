#include <iostream>
using namespace std;

int main()
{
    int a = 3.14;
    cout << a << endl;

    // (typename)a or typename(a)
    char ch = 'M';
    cout << int(ch) << " " << (int)ch << endl;

    // c++
    // static_cast<typename>
    cout << static_cast<int>(ch) << endl;

    return 0;
}