class Solution {
    public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> freq = new HashMap<>();
     
     int count = 1;
    for(int num : nums) {
      if(!freq.containsKey(num)) {
        freq.put(num,count);
        } else {
        freq.put(num, freq.get(num)+1);
        }
     }
PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>(
    (a, b) -> a.getValue() - b.getValue()
);     
     for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
      minHeap.offer(entry);
      if( minHeap.size() > k){
        minHeap.poll(); // removing the smallest value
      }
     }

       int [] topK = new int [k];
       int index = 0;
        while (!minHeap.isEmpty()) {
        topK[index++] = minHeap.poll().getKey();
        }
     return topK;
    }


    }
