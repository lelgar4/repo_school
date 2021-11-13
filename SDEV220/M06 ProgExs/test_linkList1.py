'''
    Richard Elgar
    SDEV220
    TEST for linkList1.py

    Write a test program that: 
    1. creates two lists, list1 and list2, with the initial values 
        {"Tom", "George", "Peter", "Jean", "Jane"} 
        and {"Tom", "George", "Michael", "Michelle", "Daniel"}

    2. then invokes list1.addAll(list2), list1.removeAll(list2), and list1.retainAll(list2) and displays the resulting new list1.
'''

import linkList1
from linkList1 import LinkList1
from linkList1 import Node


def setLists(names):
    linkList = LinkList1()
    for name in names:
        node = Node(name)
        linkList.add(node)
        
    return linkList
    
    


def main():
    namesList1 = ['Tom','George','Peter','Jean','Jane']
    namesList2 = ['Tom','George','Michael','Michelle','Daniel']
    list1 = setLists(namesList1)
    list2 = setLists(namesList2)


#   add all values from list2 to list1 using addAll()
    print("\n----------------\nADD ALL\n----------------\n")
    print("[T/F]: ",list1.addAll(list2))
    print("----------\nList1: ")
    for node in list1:
        print(node.element)
    
    
#       
    print("\n----------------\nREMOVE ALL\n----------------\n")
    print("[T/F]: ",list1.removeAll(list2))
    print("----------\nList1: ")
    for node in list1:
        print(node.element)
        

    print("\n----------------\nRETAIN ALL\n----------------\n")
    print("[T/F]: ",list1.retainAll(list2))
    print("----------\nList1: ")
    for node in list1:
        print(node.element)
    
    
    
    if print(list1) == -1:
        print("LinkedList is empty")
    else:
        print("\n\n\n============================================\nResult:\n")
        for node in list1:
            print(node.element)
        print("============================================")
    




main()