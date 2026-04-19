/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
 class Solution {
    public ListNode reverseList(ListNode head) {
       ListNode curr = head;
       ListNode prev = null;


    while( curr != null) {
     ListNode next =  curr.next;
      curr.next = prev;
      // basically making this point to the next current
      prev = curr;
      // prev is now equal to th head
      curr = next;
      // going to the next node
       }

       return prev;
       

     
   

    

    }
}
