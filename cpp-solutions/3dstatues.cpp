#include <iostream>

int main(){
    int n;
    int statues = 1;
    int days = 1;
    std::cin >> n;
    while(statues < n){
        statues *= 2;
        days++;
    }
    std::cout << days;
    return 0;
}