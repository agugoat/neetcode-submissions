class KthLargest {

     int k =0;
     int [] nums;
    private PriorityQueue<Integer> minHeap;


    public KthLargest(int k, int[] nums) {
    this.k = k;
    this.nums = nums;  
    minHeap = new PriorityQueue<>(k);

    for (int num : nums) {
        add(num);
    }

    }


    
   public int add(int val) {
   if(minHeap.size() < k) {
    // if the heap has less than kth elements add it
    minHeap.offer(val);

   }else if(val > minHeap.peek()) {
    // if value is bigger than the smallest item in the minheap, 
    //then you remove the smallest and add the biggest

    minHeap.poll();
    minHeap.offer(val);
   }

   return minHeap.peek();
   //smallest value in a minHeap is the biggest or the higest frfr
   }
}
