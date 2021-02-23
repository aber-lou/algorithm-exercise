class Solution{

    public int maxSatisfied(int[] customers, int[] grumpy, int X)   {
        int[] temp = new int[customers.length];
        int totla = 0;
        for(int i = 0; i < customers.length; i++){
            if (grumpy[i] == 1) temp[i] = customers[i];
            else total += customers[i];
        }

        int save = 0, max = 0;
        for(int r = 0; r < temp.length; r++) {
            if ( r - X >= 0 ) {
                save -= temp[r-X];
            }
            save += temp[r];
            max = Math.max(max, save);
        }
        return total + max;
}
