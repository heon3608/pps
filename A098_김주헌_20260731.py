# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        currA = headA
        while currA:
            lenA += 1
            currA = currA.next
            
        lenB = 0
        currB = headB
        while currB:
            lenB += 1
            currB = currB.next
            
        currA = headA
        currB = headB
        
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next
                
        while currA != currB:
            currA = currA.next
            currB = currB.next
            
        return currA