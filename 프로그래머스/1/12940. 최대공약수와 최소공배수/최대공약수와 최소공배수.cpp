#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

vector<int> solution(int n, int m) {
    unordered_set<int> set_n;
    unordered_set<int> set_m;

    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            set_n.insert(i);
            set_n.insert(n / i);
        }
    }
    for (int i = 1; i * i <= m; i++) {
        if (m % i == 0) {
            set_m.insert(i);
            set_m.insert(m / i);
        }
    }
    int gcd = 1;
    for (auto& x : set_m) {
        if (set_n.count(x) && x > gcd) {
            gcd = x;
        }
    }
    return vector<int> {gcd, n * m / gcd};
}