"""
2. Add Two Numbers
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         linked_list = ListNode()

#         ten = 0
#         temp = linked_list
#         while True:
#             if l1 == None and l2 == None:
#                 break

#             if l1 and l2:
#                 total = l1.val + l2.val + ten
#                 l1 = l1.next
#                 l2 = l2.next
#             elif l1:
#                 total = l1.val + ten
#                 # print("@", l1.val, ten)
#                 l1 = l1.next
#                 # print("@@", l1)
#             elif l2:
#                 total = l2.val + ten
#                 l2 = l2.next

#             if total >= 10:
#                 temp.val = total % 10
#                 ten = 1
#                 # print("#", total % 10)
#             else:
#                 temp.val = total
#                 ten = 0

#             if l1 != None or l2 != None or ten:
#                 temp.next = ListNode()
#                 temp = temp.next

#         if ten:
#             temp.val = ten

#         return linked_list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linked_list = ListNode()
        temp = linked_list

        total = 0
        while l1 or l2 or total:
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            temp.next = ListNode(total % 10)
            temp = temp.next
            total //= 10

        return linked_list.next
