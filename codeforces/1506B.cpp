#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;

using std::string;

int main() {
    // hell
    int n;

    int l, k;
    string s;

    int co;

    cin >> n;
    
    int start, end;
    int j;

    for (int i = 0; i < n; i++){
        cin >> l >> k;
        cin >> s; 

        for (j = 0; j < s.length(); j++){
            if (s[j] == '*'){
                start = j;
                break;
            }
        }

        for (j = s.length() - 1; j >= 0; j--){
            if (s[j] == '*'){
                end = j;
                break;
            }
        }

        if (start == end){
            cout << 1 << "\n";
            continue;
        }

        co = 2;

        bool f = true;

        while (f){
            

            if (start == end){
                f = false;
                co--;
                continue;
            }

            if (start + k + 1 >= l){
                f = false ;
                continue; 
            }

            co++;
            for (j = k; j > 0; j--){
                if (s[start + j] == '*'){
                    start += j;
                    break;
                }
            }
        }

        cout << co << "\n";

    }

    return 0;
}

