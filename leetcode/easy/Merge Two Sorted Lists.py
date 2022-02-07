#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

class Solution:
    def merge(self, merged_list, list1, list2):
        if list1 is None:
            merged_list.next = list2
            return merged_list
        elif list2 is None:
            merged_list.next = list1
            return merged_list
        
        elif list1.val <= list2.val:
            merged_list.next = list1
            merged_list = merged_list.next
            return self.merge(merged_list, list1.next, list2)
        else:
            merged_list.next = list2
            merged_list = merged_list.next
            return self.merge(merged_list, list1, list2.next)
        
    def mergeTwoLists(self, list1, list2):
        header = ListNode()
        self.merge(header, list1, list2)
        return header.next     
