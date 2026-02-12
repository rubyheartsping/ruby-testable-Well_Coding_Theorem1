#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer;
    for (auto it = my_string.rbegin(); it != my_string.rend(); ++it) {
        answer.push_back(*it);
    }
    return answer;
}