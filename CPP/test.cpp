// class Solution {
// public:
//     string smallestSubsequence(string s) {
//         unordered_map<char, int> mp;

//         for (int i = 0; i < s.size(); i++) {
//             mp[s[i]] = i;
//         }
//         //  mapping of the elements

//         stack<char> st;
//         unordered_map<char, bool> used;

//         for (int i = 0; i < s.size(); i++) {

//             if (used[s[i]])
//                 continue;

//             while ((!st.empty() && st.top() > s[i]) && mp[st.top()] > i) {
//                 used[st.top()] = false;
//                 st.pop();
//             }

//             st.push(s[i]);
//             used[s[i]]=true;
//         }

//         string ans = "";

//         while (!st.empty()) {
//             ans += st.top();
//             st.pop();
//         }

//         reverse(ans.begin(), ans.end());

//         return ans;
//     }
// };