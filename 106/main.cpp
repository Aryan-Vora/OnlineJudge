#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

pair<int, int> count_triples_and_unused(int N) {
  vector<bool> used(N + 1, false);
  int coprime_triples_count = 0;

  for (int m = 2; m * m <= N; ++m) {
    for (int n = 1; n < m; ++n) {
      if ((m - n) % 2 == 1 && __gcd(m, n) == 1) {
        int a = m * m - n * n;
        int b = 2 * m * n;
        int c = m * m + n * n;
        if (c > N) break;

        int k = 1;
        while (k * c <= N) {
          if (k == 1) {
            coprime_triples_count++;
          }
          int ka = k * a;
          int kb = k * b;
          int kc = k * c;
          if (ka <= N) used[ka] = true;
          if (kb <= N) used[kb] = true;
          if (kc <= N) used[kc] = true;
          k++;
        }
      }
    }
  }

  int not_in_any_triple_count = count(used.begin() + 1, used.end(), false);

  return {coprime_triples_count, not_in_any_triple_count};
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string line;
  vector<int> inputs;

  while (getline(cin, line)) {
    if (!line.empty()) {
      inputs.push_back(stoi(line));
    }
  }

  for (int N : inputs) {
    auto result = count_triples_and_unused(N);
    cout << result.first << " " << result.second << "\n";
  }

  return 0;
}
