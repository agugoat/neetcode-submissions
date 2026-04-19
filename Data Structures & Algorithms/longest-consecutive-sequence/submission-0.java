class Solution {
    public int longestConsecutive(int[] nums) {
         Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
       int count = 0;
        for (int num:numSet) {
          if(!numSet.contains(num-1)) {
            //beginning of a seqeunce
            int currNum = num;
            int currLength = 1;
          
          while (numSet.contains(currNum+1)){
            currNum+=1;
            currLength +=1;
          }

          count = Math.max(count, currLength);

        }
        }

      return count;
    }
}
