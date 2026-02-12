#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string) {
    string vowel = "aeiou";
    for (char c : vowel) {
        my_string.erase(remove(my_string.begin(), my_string.end(), c), my_string.end());
    }
    return my_string;
}