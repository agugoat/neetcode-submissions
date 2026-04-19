class Solution {
    public int search(int[] nums, int target) {
        
      for( int i = 0; i < nums.length; i++) {
        int curr = nums[i];
        if (curr == target) {
           return i;
        }
      }
        return -1;
      }

    }

