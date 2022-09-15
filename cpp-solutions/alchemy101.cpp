#include <iostream>

using namespace std;

int main() {
    int t, m, sol_len;
    bool skip_1, skip_m1, skip_m;
    cin >> t;
    while(t--) {
        cin >> m;
        skip_1 = skip_m1 = skip_m = false;
        if(m == 1) {
            cout << 1 << "\n" << 1 << "\n";
        } else if (m == 2) {
            cout << 1 << "\n" << 2 << "\n";
        } else {
            if(m % 4 == 0) { sol_len = m; } 
            else if(m % 4 == 1) { sol_len = m-1; skip_m1 = true;} 
            else if(m % 4 == 2) { sol_len = m-1; skip_1 = true; }
            else { sol_len = m-1; skip_m = true;}
            cout << sol_len << '\n';
            if(skip_m) {
                for(int i = 1; i < m; i++) {
                    cout << i << ' ';
                }
            } else if(skip_1) {
                for(int i = 2; i <= m; i++) {
                    cout << i << ' ';
                }
            }  else if(skip_m1) {
                for(int i = 1; i < m-1; i++) {
                    cout << i << ' ';
                }
                cout << m;
            } else {
                for(int i = 1; i <= m; i++) {
                    cout << i << ' ';
                }
            }
            cout << '\n';   
        }
    }
    return 0;
}
