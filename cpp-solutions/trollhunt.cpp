#include <iostream>

int main(){
    int b, k, g;
    std::cin >> b >> k >> g;
    b--;
    int num_groups = k/g;
    if(b % num_groups == 0){
        std::cout << b/num_groups;
    } else {
        std::cout << (b/num_groups) + 1;
    }

    return 0;
}