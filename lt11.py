回文链表的python做法


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        def list_reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        half = list_reverse(slow.next)
        p = half
        q = head
        isPalind = True
        while p:
            if p.val != q.val:
                isPalind = False
                break
            p = p.next
            q = q.next
        slow.next = list_reverse(half)
        return isPalind
# Python 统一规定，只要你想访问对象里面的属性或方法，一律用 .
