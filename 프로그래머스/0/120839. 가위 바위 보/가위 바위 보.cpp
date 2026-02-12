#include <string>
#include <vector>

using namespace std;

string solution(string rsp) {
    string answer = "";
    for (auto x : rsp) {
        if (x == '2') {
            answer += "0";
        }
        else if (x == '0') {
            answer += "5";
        }
        else if (x == '5') {
            answer += "2";
        }
    }
    return answer;
}