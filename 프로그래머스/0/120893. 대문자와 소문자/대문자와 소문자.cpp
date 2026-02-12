#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    for (char c : my_string) {
        if (c <= 90) {
            answer += c + 32;
        }
        
        else if (97 <= c) {
            answer += c - 32;
        }
    }
    return answer;
}