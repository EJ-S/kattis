#include <iostream>

int main() {
    int a, b, c, d, e, g;
    std::cin >> a >> b >> c >> d >> e >> g;
    if(g >= a) {
        std::cout << "A";
    } else if (g >= b) {
        std::cout << "B";
    } else if(g >= c) {
        std::cout << "C";
    } else if(g >= d) {
        std::cout << "D";
    } else if(g >= e) {
        std::cout << "E";
    } else {
        std::cout << "F";
    }
    return 0;
}