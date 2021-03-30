class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rowIndex = binarySearchFirstColumn(matrix, target);
        if (rowIndex < 0)  {
            return false;
        }
        return binarySearchFirstRow(matrix[rowIndex], target);
    }

    public int binarySearchFirstColumn(int[][] martrix, int target) {
        int low = -1, high = martrix.length - 1;
        while(low < high) {
            int mid = (high - low + 1) / 2 + low;
            if(martrix[mid][0] <= target) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    public boolean binarySearchFirstRow(int[] matrix, int target) {
        int low = 0, high = matrix.length - 1;
        while(low <= high) {
            int mid = (high - low) / 2 + low;
            if(matrix[mid] == target) {
                return true;
            } else if(matrix[mid] > target) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return false;
    }
}