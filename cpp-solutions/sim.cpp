#include <iostream>
#include <string>
#include <list>

int main(){
    int t;
    std::cin >> t;
    std::cin.ignore();
    while (t--){
        std::string msg;
        std::list<char> out;
        std::list<char>::iterator index = out.begin(); 
        std::getline(std::cin, msg);
        for (char c : msg){
            if (index == out.begin() && c == '<'){
                continue;    
            } else if (c == '<'){
                index = out.erase(--index);
            } else if ( c == '[') {
                index = out.begin();
            } else if (c == ']'){
                index = out.end();
            } else {
                index = out.insert(index, c);
                index++;
            }
        }
        for (char c : out){
            std::cout << c;
        }
        std::cout << '\n';
        
    }


    return 0;
}