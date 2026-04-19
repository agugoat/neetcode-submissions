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
    public boolean hasCycle(ListNode head) {
          if (head == null || head.next == null ) {
        return false; // No cycle if the list is empty or has only one element
    } 
       ListNode curr = head;
       ListNode fasfa = head.next;

     while(curr != fasfa && fasfa.next != null && fasfa.next.next != null) {
   
     curr = curr.next;
     fasfa = fasfa.next.next;
     if( curr == fasfa) {
        return true;   
     }  
    }
    return false;
}
}
