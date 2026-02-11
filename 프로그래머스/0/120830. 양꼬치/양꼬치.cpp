#include <string>
#include <vector>

using namespace std;

int solution(int n, int k) {
    return n * 12000 + (k - (int)(n / 10)) * 2000;
}