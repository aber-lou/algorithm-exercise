class Solution:
    public:
        vector<int> mostVisited(int n, vector<int>&rounds) {
            vector<int> ret;
            int size = rounds.size();
            int start = rounds[0], end = rounds[size - 1];
            if (start <= end) {
                for (int i = start; i<= end; i++){
                    ret.push_back[i];
                }
            } else {
                for (int i = 1; i <= end; i++) {
                    ret.push.back(i);
                }
                for (int i = start; i <= n; i++) {
                    ret.push_back(i);
                }
            }
            return ret;

        }