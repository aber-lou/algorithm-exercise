class Solution(object):
    def rotateRight(self, head, k):
        if k == 0 or not head or not head.next:
            return head

        l = 1
        tail = head
        while tail.next:
            l += 1
            tail = tail.next

        pos = l - k % l

        if pos == 1:
            return head
        
        curNode = head
        for _ in range(pos - 1):
            curNode = curNode.next
        

        tempHead = curNode.next
        curNode.next = None
        tail.next = head

        return tempHead

