#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int numbering(string s) {
    if (s=="code") return 0;
    if (s=="date") return 1;
    if (s=="maximum") return 2;
    if (s=="remain") return 3;
    return -1;
}

vector<vector<int>> solution(vector<vector<int>> data, string ext, int val_ext, string sort_by) {
    vector<vector<int>> answer;
    int ext_idx = numbering(ext);
    int sort_by_idx = numbering(sort_by);
    for (auto d : data) {
        if (d[ext_idx] < val_ext) {
            answer.push_back(d);
        }
    }
    sort(answer.begin(), answer.end(), [sort_by_idx](const vector<int>& a, const vector<int>& b) {
        return a[sort_by_idx] < b[sort_by_idx];
    });

    return answer;
}