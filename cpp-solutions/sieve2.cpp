#include <iostream>
#include <vector>

std::vector<bool> is_prime(100000001, true);

int main(){
    int n, q;
    std::cin >> n >> q;
    is_prime[0] = false;
    is_prime[1] = false;
    for(int i = 2; i*i <= n; i++){
        if(is_prime[i]){
            int k = i*i;
            for(int j = 0; k + (j*i) <= n; j++){
                is_prime[k+(j*i)] = false;
            }
        }
    }
    int count = 0;
    for(int i = 2; i <= n; i++){
        if(is_prime[i]){count++;}
    }
    std::cout << count << '\n';
    while(q > 0){
        int n;
        std::cin >> n;
        std::cout << is_prime[n] << '\n';
        q--;
    }
    return 0;
}