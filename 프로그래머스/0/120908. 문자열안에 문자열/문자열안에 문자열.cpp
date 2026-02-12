#include <string>
#include <vector>

using namespace std;

int solution(string str1, string str2) {
    for (int i = 0; i <= str1.size() - str2.size() + 1; i++) {
        string inspector(str1.begin() + i, str1.begin() + i + str2.size());
        if (inspector == str2) {
            return 1;
        }
    }
    return 2;
}