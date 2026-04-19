class Solution {
    public int lastStoneWeight(int[] stones) {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    int count = 0;
   
    for (int stone : stones) {
            maxHeap.offer(stone);
        }

   while(maxHeap.size() > 1) {
   int x = maxHeap.poll();
   int y = maxHeap.poll(); 
   
   if(x != y) {
     int newY = x-y;
    maxHeap.offer(newY);

   }

   }

   if (maxHeap.size() == 1) {
    return maxHeap.poll();
   } else {
    return 0;
   }

   

    }
}
