# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Inline function to reverse a list recursively upto a cetain count
        def reverse(head: Optional[ListNode], count: int) -> Optional[ListNode]:
            if not head: # Probably a redundant case if we can assume that left and right are within bounds
                return None, None

            # Since the pointers are 1-indexed, we count till 1
            if not head.next or count == 1:
                return head, head.next

            # Get the new head and its next node, it will propagate back to the start
            new_head, new_head_next = reverse(head.next, count - 1)
            head.next.next = head
            head.next = None
            return new_head, new_head_next
        
        # Dummy node always helps
        dummy = ListNode()
        dummy.next = head
        one_behind = dummy
        while left > 1:
            head = head.next
            one_behind = one_behind.next
            left -= 1
            right -= 1

        new_head, new_head_next = reverse(head, right)

        one_behind.next = new_head
        head.next = new_head_next
        return dummy.next
        
