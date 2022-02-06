class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        if head.next is None and head.val == val:
            return None
        
        if head.next is None and head.val != val:
            return head
        
        prev = None
        curr = head
        while curr:
            if curr.val == val and prev is not None:
                prev.next = curr.next
                curr = curr.next
            elif curr.val == val and prev is None:
                head = curr.next
                prev = None
                curr = head
                
            else:
                prev = curr
                curr = curr.next
        
        return head

            

head = ListNode(1)
second = ListNode(2)
third = ListNode(6)
four = ListNode(3)
five = ListNode(4)
six = ListNode(5)
seven = ListNode(6)

# head = ListNode(1)
# second = ListNode(2)
# third = ListNode(2)
# four = ListNode(1)

head.next = second
second.next = third
third.next = four
four.next = five
five.next = six
six.next = seven

res = Solution()
demo = res.removeElements(head, 6)

while demo != None:
    print(demo.val)
    demo = demo.next
