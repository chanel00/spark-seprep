class Solution:
    def mergeTwoLists(self, l1,l2):
        # Base: if 1 list is empty, return other
        if not l1:
            return l2
        elif not l2:
            return l1

        # Recursive: compare current nodes
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2