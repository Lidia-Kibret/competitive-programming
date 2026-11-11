# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        result = []
        ans = head 
        while ans:
            result.append(ans.val)
            ans = ans.next
        return result == result[::-1]



        