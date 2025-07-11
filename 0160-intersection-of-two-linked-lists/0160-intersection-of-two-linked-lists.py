# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        value = set()
        currentA = headA
        while currentA:
            value.add(currentA)
            currentA = currentA.next
        currentB = headB
        while currentB:
            if currentB in value:
                return currentB 
            currentB = currentB.next

        return None 
        