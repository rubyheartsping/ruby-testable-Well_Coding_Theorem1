#include <string>
#include <iostream>
using namespace std;

bool solution(string s) {
    int cnt1 = 0;
    int cnt2 = 0;
    for (char x : s) {
        if (x == 'p' || x == 'P') {
            cnt1++;
        }
        
        else if (x == 'y' || x == 'Y') {
            cnt2++;
        }
    }
    if (cnt1 == cnt2) {
        return true;
    }
    
    else if (cnt1 != cnt2) {
        return false;
    }
}