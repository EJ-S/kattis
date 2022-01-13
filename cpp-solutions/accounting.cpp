#include <iostream>
#include <algorithm>
#include <string>

int main() {
    int N, Q;
    std::cin >> N >> Q;
    int money[N];
    int whenSet[N];
    std::fill_n(money, N, 0);
    std::fill_n(whenSet, N, 0);
    int restart = 0, restartSet = -1;
    for(int i = 0; i < Q; i++) {
        std::string task;
        std::cin >> task;
        int person, value;
        if(task == "SET") {
            std::cin >> person >> value;
            money[person - 1] = value;
            whenSet[person - 1] = i+1;
        } else if(task == "RESTART") {
            std::cin >> value;
            restart = value;
            restartSet = i+1;
        } else {
            std::cin >> person;
            if(whenSet[person - 1] > restartSet) {
                std::cout << money[person - 1] << "\n";
            } else {
                std::cout << restart << "\n";
            }
        }
    }
    return 0;
}