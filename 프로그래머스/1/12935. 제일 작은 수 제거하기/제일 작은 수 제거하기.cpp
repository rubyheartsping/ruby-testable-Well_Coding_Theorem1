#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    int mn = *min_element(arr.begin(), arr.end());
    arr.erase(remove(arr.begin(), arr.end(), mn), arr.end());
    if (arr.size() == 0) return vector<int> {-1};
    return arr;
}