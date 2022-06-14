class PatternMatching  {

    public static int getIndexOf(String s, String m) {
        if (s == null || m == null || m.length() < 1 || s.length() < m.length()) {
            return -1;
        }

        char[] str1 = s.toCharArray();
        char[] str2 = m.toCharArray();
        int[] next = NextSum(str2);

        int l1 = 0;
        int l2 = 0;

        while(l1 < str1.length && l2 < str2.length) {
            if(str1[l1] == str2[l2]) {
                l1 += 1;
                l2 += 1;
            } else if(next[l2] == -1) {
                l1 += 1;
            } else {
                l2 = next[l2];
            }
        }
        return l2 == str2.length ? l1 - l2 : -1;  
    }

    //  求解Next数组
    public static int[] NextSum(char[] ms) {
        if(ms.length == 1) {
            return new int[] { -1 };
        }
        // Next数组默认填-1
        int [] next = new int[ms.length];
        next[0] = -1;   // Next 数组第一个值为-1
        next[1] = 0;
        int i = 2;
        /// Next数组匹配值
        int cn = 0;
        while(i < next.length) {
            if( ms[i - 1] == ms[cn] ) {
                next[i] = cn + 1;
                i += 1;
                cn += 1;
            } else if(cn > 0) {
                cn = next[cn];
            } else {
                next[i++] = 0;
            }
        }
        return next;
    }
}

