class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1, list2):
        if(list1 == None):
            return list2
        elif list2 == None:
            return list1

        if(list1.val > list2.val):
            res = ListNode(list2.val)
            list2 = list2.next
        else:
            res = ListNode(list1.val)
            list1 = list1.next
        resCopy = res
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                tmp = ListNode(list2.val)
                resCopy.next = tmp
                resCopy = resCopy.next
                list2 = list2.next
            else:
                tmp = ListNode(list1.val)
                resCopy.next = tmp
                resCopy = resCopy.next
                list1 = list1.next
        if(list1 == None):
            while list2 != None:
                tmp = ListNode(list2.val)
                resCopy.next = tmp
                resCopy = resCopy.next
                list2 = list2.next
        elif list2 == None:
            while list1 != None:
                tmp = ListNode(list1.val)
                resCopy.next = tmp
                resCopy = resCopy.next
                list1 = list1.next
        return res


list1 = ListNode(1)
second = ListNode(2)
third = ListNode(4)
list1.next = second
second.next = third

list2 = ListNode(1)
second = ListNode(3)
third = ListNode(4)
list2.next = second
second.next = third


res = Solution()
demo = res.hasCycle(list1, list2)

while demo != None:
    print(demo.val)
    demo = demo.next