# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next:
            gcd = math.gcd(head.val, head.next.val)
            node = ListNode(gcd, head.next)
            head.next = node
            self.insertGreatestCommonDivisors(head.next.next)
        return head
