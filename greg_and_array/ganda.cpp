#include <iostream>
#include <vector>
using namespace std;

void solution(vector<vector<int>>& operations, vector<int>& arr, 
              vector<vector<int>>& queries, int n, int m, int k) {
    // initialize array of size n + 2
    vector<long long> diff_arr(n + 2, 0);
    
    // populate difference array
    for (auto& q : queries) {
        for (int i = q[0]; i <= q[1]; i++) {
            auto& op = operations[i - 1];  // convert to 0-indexed
            diff_arr[op[0]] += op[2];
            diff_arr[op[1] + 1] -= op[2];
        }
    }
    
    // compute prefix sum
    vector<long long> p(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        p[i] = p[i - 1] + diff_arr[i];
    }
    
    // output final array
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] + p[i + 1];
        if (i < arr.size() - 1) cout << " ";
    }
    cout << "\n";
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    vector<vector<int>> operations(m, vector<int>(3));
    for (int i = 0; i < m; i++) {
        cin >> operations[i][0] >> operations[i][1] >> operations[i][2];
    }
    
    vector<vector<int>> queries(k, vector<int>(2));
    for (int i = 0; i < k; i++) {
        cin >> queries[i][0] >> queries[i][1];
    }
    
    solution(operations, arr, queries, n, m, k);
    
    return 0;
}
