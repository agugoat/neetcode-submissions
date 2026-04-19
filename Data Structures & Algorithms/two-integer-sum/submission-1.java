class Solution {
    public int[] twoSum(int[] nums, int target) {
  //Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] + nums[i] == target) {
                    return new int[]{i, j}; // Return the indices of the pair that adds up to the target
                }
            }
        }
        return new int[]{}; // Return an empty array if no pair is found
    }
}
