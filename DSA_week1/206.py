class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        prevPtr = None
        flag = False
        while head != None:
            nxtPtr = head.next
            if(head.next == None and flag == True):
                head.next = prevPtr
                return head
            head.next = prevPtr
            prevPtr = head
            head = nxtPtr
            flag = True

            

head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
four = ListNode(4)
five = ListNode(5)
# six = ListNode(5)
# seven = ListNode(6)

# head = ListNode(1)
# second = ListNode(2)
# third = ListNode(2)
# four = ListNode(1)

head.next = second
second.next = third
third.next = four
four.next = five
# five.next = six
# six.next = seven

res = Solution()
demo = res.reverseList(head)

while demo != None:
    print(demo.val)
    demo = demo.next
