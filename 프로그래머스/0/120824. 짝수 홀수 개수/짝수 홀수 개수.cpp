#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer = {0, 0};
    for (auto x : num_list) {
        if (x % 2 == 1) {
            answer[1]++;
        }
        
        else if (x % 2 == 0) {
            answer[0]++;
        }
    }
    return answer;
}