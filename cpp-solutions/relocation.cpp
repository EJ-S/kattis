#include <iostream>
#include <bits/stdc++.h>
#include <stdlib.h>

int main() {
    int n;
    int q;
    std::cin >> n >> q;
    int locations [n] = {};
    for(int i = 0; i < n; i++){
        int loc;
        std::cin >> loc;
        locations[i] = loc;
    }
    for(int i = 0; i < q; i++){
        int first;
        int second;
        int third;
        std::cin >> first >> second >> third;
        if(first == 1){
            locations[second-1] = third;
        } else {
            std::cout << abs(locations[second-1] - locations[third-1]) << std::endl;
        } 
    }
}
