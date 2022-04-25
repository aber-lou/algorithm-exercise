class Solution {
    int[][] memo;

    public int minDistance(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        memo = new int[m][n];

        for (int[] row : memo) {
            Arrays.fill(row, - 1);
        }
        return dp(s1, m - 1, s2 , n - 1);
    }

    int dp(String s1, int i, String s2, int j) {
        if (j == -1) return i + 1;
        if (i == -1) return j + 1;

        if (memo[i][j] != -1) {
            return memo[i][j];
        }

        if (s1.charAt(i) == s2.charAt(j) ){
            memo[i][j] = dp(s1, i - 1, s2, j - 1);
        } else {
            memo[i][j] = Math.min(
                dp(s1, i, s2, j - 1) + 1,
                    Math.min(
                        dp(s1, i - 1, s2, j ) + 1,
                        dp(s1, i - 1, s2, j - 1) + 1
                    )
            );
        }
        return memo[i][j];
    }

    public int minDistance2(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();

        if (n * m == 0 ) {
            return n + m;
        }

        int[][] dp = new int[n + 1][m + 1];

        for(int i = 0; i < n + 1; i++) {
            dp[i][0] = i;
        }

        for(int j = 0; j < m + 1; j++ ){
            dp[0][j] = j;
        }

        for(int i = 1; i < n + 1; i++) {
            for(int j = 1; j < m + 1; j++) {
                int left = dp[i - 1][j] + 1;
                int down = dp[i][j - 1] + 1;
                int left_down = dp[i - 1][j - 1];
                if (word1.charAt(i) != word2.charAt(j)) {
                    left_down += 1;
                }
                dp[i][j] = Math.min(left, Math.min(down, left_down));
            }
        }

        return dp[m][n];
    }
}