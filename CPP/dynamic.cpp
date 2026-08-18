#include <bits/stdc++.h>
using namespace std;

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // ============================================================
    // RANK 1
    // VECTOR / ARRAY
    // ============================================================

    // CASE A: N IS GIVEN
    int n;
    cin >> n;

    vector<int> arr(n);

    for (auto &x : arr)
        cin >> x;

    /*
    INPUT:
    5
    10 20 30 40 50
    */

    // CASE B: VECTOR DIRECTLY GIVEN
    // No N, entire remaining input belongs to vector

    vector<int> v;
    int x;

    while (cin >> x)
        v.push_back(x);

    /*
    INPUT:
    10 20 30 40 50
    */

    // ============================================================
    // RANK 2 ⭐⭐⭐⭐⭐
    // STRING
    // ============================================================

    string s;
    cin >> s;

    /*
    INPUT:
    hello
    */

    // ============================================================
    // RANK 3 ⭐⭐⭐⭐⭐
    // VECTOR OF STRINGS
    // ============================================================

    int n2;
    cin >> n2;

    vector<string> words(n2);

    for (auto &word : words)
        cin >> word;

    /*
    INPUT:
    3
    apple banana mango
    */

    // ============================================================
    // RANK 3B ⭐⭐⭐⭐
    // VECTOR OF CHAR
    // ============================================================

    int n3;
    cin >> n3;

    vector<char> chars(n3);

    for (auto &ch : chars)
        cin >> ch;

    /*
    INPUT:
    5
    a b c d e
    */

    // ============================================================
    // RANK 4 ⭐⭐⭐⭐⭐
    // MULTIPLE TEST CASES
    // ============================================================

    int t;
    cin >> t;

    while (t--)
    {

        int n;
        cin >> n;

        vector<int> arr(n);

        for (auto &x : arr)
            cin >> x;

        // solve current test case
    }

    /*
    INPUT:

    3

    5
    1 2 3 4 5

    3
    10 20 30

    4
    7 8 9 10
    */

    // ============================================================
    // RANK 5 ⭐⭐⭐⭐
    // MATRIX / 2D VECTOR
    // ============================================================

    int rows, cols;
    cin >> rows >> cols;

    vector<vector<int>> mat(
        rows,
        vector<int>(cols));

    for (auto &row : mat)
        for (auto &x : row)
            cin >> x;

    /*
    INPUT:

    3 3

    1 2 3
    4 5 6
    7 8 9
    */

    // ============================================================
    // RANK 6 ⭐⭐⭐⭐
    // PAIRS / INTERVALS
    // ============================================================

    int k;
    cin >> k;

    vector<pair<int, int>> pairs(k);

    for (auto &p : pairs)
        cin >> p.first >> p.second;

    /*
    INPUT:

    3
    1 5
    2 7
    4 9
    */

    // ============================================================
    // RANK 7 ⭐⭐⭐⭐
    // GRAPH - UNWEIGHTED
    // ============================================================

    int V, E;
    cin >> V >> E;

    vector<vector<int>> adj(V + 1);

    for (int i = 0; i < E; i++)
    {

        int u, v;
        cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    /*
    INPUT:

    5 4

    1 2
    1 3
    2 4
    3 5
    */

    // ============================================================
    // RANK 7B ⭐⭐⭐
    // WEIGHTED GRAPH
    // ============================================================

    int V2, E2;
    cin >> V2 >> E2;

    vector<vector<pair<int, int>>> graph(V2 + 1);

    for (int i = 0; i < E2; i++)
    {

        int u, v, w;
        cin >> u >> v >> w;

        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }

    // ============================================================
    // RANK 8 ⭐⭐⭐
    // LONG LONG
    // ============================================================

    long long num;
    cin >> num;

    vector<long long> bigArr(n);

    for (auto &x : bigArr)
        cin >> x;

    // ============================================================
    // RANK 8B ⭐⭐⭐
    // DOUBLE
    // ============================================================

    double decimal;
    cin >> decimal;

    // ============================================================
    // RANK 9 ⭐⭐⭐
    // STRING WITH SPACES
    // getline()
    // ============================================================

    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string line;
    getline(cin, line);

    /*
    INPUT:

    hello bro this is a sentence
    */

    // ============================================================
    // RANK 10 ⭐⭐
    // READ UNTIL EOF
    // ============================================================

    int value;

    while (cin >> value)
    {

        // process value
    }

    // ============================================================
    // RANK 10B ⭐⭐
    // READ UNTIL SPECIAL VALUE
    // ============================================================

    while (cin >> value && value != -1)
    {

        // process value
    }

    /*
    INPUT:

    10
    20
    30
    -1
    */

    return 0;
}

/*
================================================================
              COMPLETE OA EXAMPLE
              LEETCODE 739 - DAILY TEMPERATURES
================================================================

Suppose OA gives:

INPUT:
6
73 74 75 71 69 72

OUTPUT:
1 1 4 2 1 0

In LeetCode, input handling is hidden.

In an OA, you may have to write EVERYTHING.
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{

    // ============================================================
    // 1. FAST INPUT / OUTPUT
    // ============================================================

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // ============================================================
    // 2. INPUT
    // ============================================================

    int n;
    cin >> n;

    vector<int> temperatures(n);

    for (auto &x : temperatures)
        cin >> x;

    // ============================================================
    // 3. SOLUTION
    // ============================================================

    vector<int> ans(n, 0);

    stack<int> st;

    for (int i = 0; i < n; i++)
    {

        while (!st.empty() &&
               temperatures[st.top()] < temperatures[i])
        {

            int index = st.top();
            st.pop();

            ans[index] = i - index;
        }

        st.push(i);
    }

    // ============================================================
    // 4. OUTPUT
    // ============================================================

    for (auto &x : ans)
        cout << x << " ";

    cout << '\n';

    return 0;
}

/*
================================================================
                 MOST IMPORTANT OA TEMPLATE
================================================================

#include <bits/stdc++.h>
using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // INPUT


    // SOLUTION


    // OUTPUT

    return 0;
}


VECTOR:

int n;
cin >> n;

vector<int> arr(n);

for(auto &x : arr)
    cin >> x;


STRING:

string s;
cin >> s;


VECTOR OF STRINGS:

int n;
cin >> n;

vector<string> arr(n);

for(auto &x : arr)
    cin >> x;


MATRIX:

int n, m;
cin >> n >> m;

vector<vector<int>> mat(n, vector<int>(m));

for(auto &row : mat)
    for(auto &x : row)
        cin >> x;


TEST CASES:

int t;
cin >> t;

while(t--) {

    // input
    // solution
    // output

}


PAIR:

int n;
cin >> n;

vector<pair<int,int>> arr(n);

for(auto &p : arr)
    cin >> p.first >> p.second;


GRAPH:

int V, E;
cin >> V >> E;

vector<vector<int>> adj(V + 1);

for(int i = 0; i < E; i++) {

    int u, v;
    cin >> u >> v;

    adj[u].push_back(v);
    adj[v].push_back(u);
}

================================================================
*/