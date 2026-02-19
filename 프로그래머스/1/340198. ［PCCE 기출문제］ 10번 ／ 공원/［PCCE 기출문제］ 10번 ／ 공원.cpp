#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> mats, vector<vector<string>> park) {
    sort(mats.begin(), mats.end(), greater<int>());

    int R = (int)park.size();
    int C = R ? (int)park[0].size() : 0;

    for (int mat : mats) {
        if (mat > R || mat > C) continue;  // ✅ 공원보다 크면 스킵

        for (int i = 0; i + mat <= R; i++) {
            for (int j = 0; j + mat <= C; j++) {

                bool ok = true;
                for (int m = 0; m < mat && ok; m++) {
                    for (int n = 0; n < mat; n++) {
                        if (park[i + m][j + n] != "-1") {
                            ok = false;
                            break;
                        }
                    }
                }

                if (ok) return mat;
            }
        }
    }
    return -1;
}
