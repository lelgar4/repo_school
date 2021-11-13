'''
    Richard Elgar
    SDEV220
    Implement LinkedList
    
    Tests methods implemented in file 'linkList2.py'
'''


from typing import List
from linkList2 import LinkList2
from linkList2 import Node


def main():
    namesList = ['Tom','George','Peter','Jean','Jane','Tom','George','Michael','Michelle','Daniel']
    
    linkedList = LinkList2()
    for i in range(namesList.__len__() -1):
        linkedList.add(Node(namesList[i]))
     

    print(linkedList.indexOf('Peter'))
    print(linkedList.getSize())
    print(linkedList.get(2))
    
    print("\n------------\nEX: lastIndexOf()")
    print(linkedList.lastIndexOf('Tom'))
    
    print("\n------------\nEX: set()")
    print(linkedList.get(1))
    linkedList.set(1,"--")
    print(linkedList.get(1))
    
    print("\n------------\nEX: remove()")
    linkedList.remove("--")
    print(linkedList.getSize())
    print(linkedList.get(1))
    
    
main()