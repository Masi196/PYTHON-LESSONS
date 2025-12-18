

class ListNode:
    def __init__(self, val=0, next= None):
        self.val= val
        self.next = next

def mergeTwoLists(list1, list2):
    
    #if one list is empthy, check the other


    if not list1:
        return list2
    if not list2:
        return list1
    


    #starting with smaller value first
    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next


    #keeping track of where we are in the new list

    current = head


    ##go through both lists

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next


        #attach remaining part
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return head
    


list1 = [1,2,4]
list2 = [1,3,4]




    
















list1 = [1, 2, 4]
list2 = [1, 3, 4]