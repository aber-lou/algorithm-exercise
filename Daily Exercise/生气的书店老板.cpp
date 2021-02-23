class Solution {
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int X) {
        int n = customers.size();
        int tot_sum = 0;
        for (int i = 0; i < n; i ++)        //统计当前满意人数
            if (grumpy[i] == 0)
                tot_sum += customers[i]; 

        int max_increase = 0;               
        for (int R = 0; R < X; R ++)        //初始化，最大可增加的满意人数(第一个窗口)
            max_increase += customers[R] * grumpy[R];

        int window_inc = max_increase;
        for (int R = X; R < n; R ++)        //sliding window 一次加R端，弹出L端
        {
            int L = R - X;
            window_inc += (- grumpy[L] * customers[L] + grumpy[R] * customers[R]);
            max_increase = std::max(max_increase, window_inc);
        }

        return tot_sum + max_increase;

    }
}