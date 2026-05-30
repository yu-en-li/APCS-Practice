// APCS Title: a244. 完全奇數
// APCS Complexity: O(1)
// APCS Tag: 條件判斷, 數學與數論, 基礎語法
// APCS Difficulty: 1

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

using ll = long long;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n, a;
  ll b, c;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a >> b >> c;
    if (a == 1)
      cout << b + c << '\n';
    else if (a == 2)
      cout << b - c << '\n';
    else if (a == 3)
      cout << b * c << '\n';
    else if (a == 4)
      cout << b / c << '\n';
  }

  return 0;
}
