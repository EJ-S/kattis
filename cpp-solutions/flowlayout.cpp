#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main() {
    int w;
    while(true) {
        cin >> w; if(w == 0) break; int width; int height; int row_width = 0; int row_height = 0;
        int max_width = 0; int max_height = 0;
        while(true) {
            cin >> width; cin >> height; 
            if(width == -1 && height == -1) {
                max_height += row_height;
                max_width = max(max_width, row_width);
                break;
            }
            if(row_width + width > w) {
                max_height += row_height; max_width = max(max_width, row_width);
                row_width = width; row_height = height;
            }
            else {
                row_width += width;
                row_height = max(row_height, height);
            }
            //cout << "MAX: " << max_width << " x " << max_height << "\n";
            //cout << "ROW: " << row_width << " x " << row_height << "\n";
        }
        cout << max_width << " x " << max_height << "\n";
    }
        return 0;
}
