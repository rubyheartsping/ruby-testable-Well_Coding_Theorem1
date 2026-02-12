#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    string s = to_string(n);
    for (auto x : s) {
        answer += (int)(x - 48);
    }
    return answer;
}