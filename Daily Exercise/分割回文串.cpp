class Solution {

public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        int n = s.size();
        if (n <= 0)
        {
            return ans;
        }

        // 临时结果的保存
        vector<string> paths;
        dfs(s, n, paths, ans, 0);
        return ans;
    }

    //判断当前字符是否是回文：双指针做法
    inline bool IsPalindrome(const string& currStr)
    {
        int l = 0;
        int r = currStr.size()-1;
        // 双指针，从字符串两边收缩去检查
        while(l < r)
        {
            if (currStr[l] != currStr[r])
            {
                return false;
            }
            l++;
            r--;
        }

        return true;
    }

    void dfs(const string& s, int n, vector<string>& paths, vector<vector<string>>& ans, int pos)
    {
        if (pos >= n)
        {
            // 回溯结束，把当前全部结果paths都保存下来
            ans.push_back(paths);
        }
        else
        {
            string currStr;
            // i表示字符串结束的位置，范围是 pos 到 n-1
            for (int i = pos; i < n; ++i)
            {
                currStr = s.substr(pos, i-pos+1);
                if (IsPalindrome(currStr))
                {
                    // 是的话加到结果里
                    paths.push_back(currStr);
                    dfs(s, n, paths, ans, i+1);
                    // 当前情况遍历完需要回溯
                    paths.pop_back();
                }
            }
        }
    }
};