"""
19. Remove Nth Node From End of List
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        print(head)
        fast = slow = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return head


if __name__ == "__main__":
    solution = Solution()
    heads = [[1, 2, 3, 4, 5], [1], [1, 2]]
    nums = [2, 1, 1]
    output = [[1, 2, 3, 5], [], [1]]

    for h, n in zip(heads, nums):
        print("#", solution.removeNthFromEnd(h, n))
