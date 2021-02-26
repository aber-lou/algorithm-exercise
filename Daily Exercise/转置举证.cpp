class Solution {
    public: 
        vector<vector<int>> transpose(vector<vector<int>>& matrix) {
            vector<vector<int>>ans;
            for(int i = 0; i < matrix[0].size(); i++){
                ans.push_back({});
                for(int j = 0; j < matrix.size(); j++){
                    ans[i].push_back(matrix[j][i]);
                }
            }
            return ans;
        }
}