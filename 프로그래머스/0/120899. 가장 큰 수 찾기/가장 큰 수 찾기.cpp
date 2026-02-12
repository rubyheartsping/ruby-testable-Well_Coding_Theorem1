#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array) {
    vector<int> array_copy = array;
    sort(array_copy.begin(), array_copy.end());
    for (int i = 0; i < array.size(); i++) {
        if(array_copy[array_copy.size() - 1] == array[i]) {
            return vector<int> {array[i], i};
        }
    }
}