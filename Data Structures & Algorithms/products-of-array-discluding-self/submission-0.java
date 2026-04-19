class Solution {
    public int[] productExceptSelf(int[] nums) {
    ArrayList<Integer> lst = new ArrayList<>();
    ArrayList<Integer> prodlist = new ArrayList<>();

    
     //adding all elements in nums to array for easier manipluation
    for(int num : nums) {
     lst.add(num);
    }

    int currIndex = 0;  // probably have to replace with I
    int [] output = new int [nums.length];

    for (int i = 0; i < lst.size(); i++) {
     int temp = lst.get(i);
     lst.remove(i);
     int product = 1; 
     for(int num : lst) {
        product *= num;
     }
     prodlist.add(product);
     lst.add(i, temp);
    }

      for (int i = 0; i < output.length; i++) {
       output[i] = prodlist.get(i);
      }

        return output;
    }
}  
