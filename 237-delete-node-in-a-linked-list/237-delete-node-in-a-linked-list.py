# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        '''temp = node.next # making a temp pointer to save the next node.
        node.val = temp.val # copying the value of next node value to the current node.
        node.next = temp.next # update the reference to the next to next node.
        '''
        node.val = node.next.val # copying next node value in the currernt node.
        node.next = node.next.next # to delete the next node that we copied, we are updating the reference of the node to next to next node.
        