class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        

class Solution:
    def mergeTwoLists(self,l1: ListNode, l2: ListNode) -> ListNode:
        
        mergeList = ListNode()
        temp = mergeList
        while(l1 and l2):
            if(l2.val < l1.val):
                temp.next = l2
                l2 = l2.next
            else:
                temp.next = l1
                l1 = l1.next
            
            temp = temp.next
        
        temp.next = l1 if l1 is not None else l2

        return mergeList.next

    def mergeTwoListPlanB(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoListPlanB(self,l1.next,l2)
        else:
            l2.next = self.mergeTwoListPlanB(self,l1,l2.next)
            
    def __init__(self) -> None:
        self.mergeTwoListPlanB()


if __name__ == "__main__":
    s = Solution()