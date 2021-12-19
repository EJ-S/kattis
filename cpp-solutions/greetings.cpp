
#include <iostream>
#include <bits/stdc++.h>
#include <string>

int main(){
    std::string greeting;
    std::cin >> greeting;
    int num_e = std::count(greeting.begin(), greeting.end(), 'e');
    std::string responce = "hy";
    responce.insert(1,num_e*2,'e');
    std::cout  << responce << std::endl;
    return 0;
}