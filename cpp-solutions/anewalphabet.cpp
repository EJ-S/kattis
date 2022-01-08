#include <iostream>
#include <string>

int main(){
    std::string translate;
    std::getline(std::cin, translate);
    int code;
    for(int i = 0; i < translate.length(); i++){
        code = int(translate[i]);
        if(code <= 90 && code >= 65){code += 32;}
        if(code < 97 || code > 122){
            std::cout << char(code);
        } else {
            switch (code){
                case 97 :
                    std::cout << '@';
                    break;
                case 98 :
                    std::cout << 8;
                    break;
                case 99 :
                    std::cout << '(';
                    break;
                case 100 :
                    std::cout << "|)";
                    break;
                case 101 :
                    std::cout << '3';
                    break;
                case 102 :
                    std::cout << '#';
                    break;
                case 103 :
                    std::cout << 6;
                    break;
                case 104 :
                    std::cout << "[-]";
                    break;
                case 105 :
                    std::cout << '|';
                    break;
                case 106 :
                    std::cout << "_|";
                    break;
                case 107 :
                    std::cout << "|<";
                    break;
                case 108 :
                    std::cout << 1;
                    break;
                case 109 :
                    std::cout << "[]\\/[]";
                    break;
                case 110 :
                    std::cout << "[]\\[]";
                    break;
                case 111 :
                    std::cout << 0;
                    break;
                case 112 :
                    std::cout << "|D";
                    break;
                case 113 :
                    std::cout << "(,)";
                    break;
                case 114 :
                    std::cout << "|Z";
                    break;
                case 115 :
                    std::cout << '$';
                    break;
                case 116 :
                    std::cout << "\'][\'";
                    break;
                case 117 :
                    std::cout << "|_|";
                    break;
                case 118 :
                    std::cout << "\\/";
                    break;
                case 119 :
                    std::cout << "\\/\\/";
                    break;
                case 120 :
                    std::cout << "}{";
                    break;
                case 121 :
                    std::cout << "`/";
                    break;
                case 122 :
                    std::cout << 2;
                    break;        
                default :
                    break;
            }
        }
    }
    return 0;
}
