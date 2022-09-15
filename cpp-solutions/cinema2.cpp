#include <string>
#include <iostream>

using namespace std;
int main()
{
    int n, m = 0; cin >> n >> m;
    int rem = m;
    int cur = 0;

    for (int i = 0; i < m; i++)
    {
        int x; cin >> x;
        if (cur + x > n)
        {
            cout << rem;
            break;
        } else 
        {
            cur += x;
        }
        rem--;
    }
}
