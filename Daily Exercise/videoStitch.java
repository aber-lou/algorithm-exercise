import java.util.Arrays;

public class videoStitch {
    int videoStitching(int[][] clips, int T) {
        if (T == 0) return 0;

        Arrays.sort(clips, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] -b[0];
        });

        int res = 0;
        int curEnd = 0, nextEnd = 0;
        int i = 0, n = clips.length;
        while (i < n && clips[i][0] <= curEnd) {
            while(i < n && clips[i][0] <= curEnd) {
                nextEnd = Math.max(nextEnd, clips[i][1]);
                i++;
            }
            res++;
            curEnd = nextEnd;
            if (curEnd >= T) {
                return res;
            }
        }
        return -1;
    }
}
