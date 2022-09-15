#include <bits/stdc++.h>
using namespace std;

int main() {
    string name; cin >> name;
    string output = "";
    output += name[0];
    for(int i = 0; i < name.size()-1; i++) {
        if(name[i+1] != name[i])
            output += name[i+1];
    }
    cout << output << "\n";
    return 0;
}
