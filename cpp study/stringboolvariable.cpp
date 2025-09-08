#include <iostream>
using namespace std;

int main()
{
    int a = 77;
    char b = a;
    char c = 'a'; // 작은 따옴표

    cout << b << endl;
    cout << c << endl;

    char d[] = "a";
    cout << d << endl;

    //bool
    // 0 : false
    // 1 : true

    bool e = 0;
    bool f = 1;
    bool g = 10;

    cout << e << " " << f << " " << g << endl;
    return 0;
}