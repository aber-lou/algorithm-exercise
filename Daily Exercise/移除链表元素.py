class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

    def pNode(self,node = None):
        if node == None:
            return
        print(node.val)
        self.pNode(node.next)

class Solution:
    def removeElements(self, head:ListNode, val: int) -> ListNode:
        if head == None:
            return head
        head.next = self.removeElements(head.next,val)
        return head.next if (head.val == val) else head

    def __init__(self):
        node = ListNode(2)
        node.next = ListNode(3)
        node.next.next = ListNode(4)
        node.next.next.next = ListNode(3)
        node = self.removeElements(node,3)
        node.pNode(node)

if __name__ == "__main__":
    s = Solution()
    