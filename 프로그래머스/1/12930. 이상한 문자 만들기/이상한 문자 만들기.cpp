#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string s) {
    string answer = "";
    int check = 0;
    for (char c : s) {
        if (c != ' ') {
            if (check % 2 == 0) {
                c = toupper(c);
                answer += c;
                check += 1;
            }
            else if  (check % 2 == 1) {
                c = tolower(c);
                answer += c;
                check += 1;    
            }
        }
        else if (c == ' ') {
            answer += c;
            check = 0;
        }
    }
    return answer;
}