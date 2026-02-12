#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    string stars;
    for (int i = 1; i <= n; i++) {
        stars += "*";
        cout << stars << "\n";
    }
    return 0;
}