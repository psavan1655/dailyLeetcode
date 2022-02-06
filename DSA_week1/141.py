class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        hashedMap = set()
        while head != None:
            if(head in hashedMap):
                return True
            else:
                hashedMap.add(head)
            head = head.next
        return False


    ######### Floyd's cycle detection algorithm ###########
    # def hasCycle(self, head):
    #     if head:
    #     slow = head
    #     fast = head.next

    #     while fast and slow and fast.next:

    #         if fast == slow:
    #             return True

    #         slow = slow.next
    #         fast = fast.next.next
            
    #     return False


head = ListNode(1)
second = ListNode(3)
third = ListNode(6)

head.next = second
second.next = third

res = Solution()
print(res.hasCycle(head))