class Solution {
    public int maxProfit(int[] prices) {
           // starting from the minium index
     int min = prices[0];
     // we could start from prices[0], but we just tryna get the maxiumn number
     int max = 0;

     for(int i = 0; i< prices.length; i++) {
     
     int currindex = prices[i];
      
      min = Math.min(currindex, min);
       
       max = Math.max(max, currindex - min);
     }
     return max;
     }

    
}
