'''
    Richard Elgar
    SDEV220
    Implemenet set operations in LinkedList

     Modify LinkedList to implement the following set methods:

            def addAll(self, otherList):
        
            def removeAll(self, otherList):

            def retainAll(self, otherList):
'''

from LinkedList import LinkedList
from LinkedList import Node
from LinkedList import LinkedListIterator


#   class 'LinkList1' extends class 'LinkedList' and adds additional functionalities
class LinkList1(LinkedList):

#   class constructor
    def __init__(self):
        super().__init__()
        self.__head = None
        self.__tail = None
        self.__size = 0
    

#   returns the index of the first occurence of a value in a LinkList1 instance; if the value is not found, returns -1
    def indexOf(self,e):
        result = 0
        for element in self:
            if element == e:
                return result
            else:
                result += 1
            
        return -1


#   overridden indexOf; includes number of elements in LinkList1 instance as parameter
    def indexOf(self,e,listLength):
        result = 0

        if listLength <= 0:
            return -1

        for element in self:
            if element == e:
                return result
            else:
                if (result + 1) <= listLength:
                    return -1
                else:
                    result += 1
            
        return -1


#   print all values in LinkList1 instance
    def __str__(self):
        try:
            listSize = self.getSize()
            result = "["
            current = self.__head

            for i in range(self.getSize()):
                result += str(current.element)
                current = current.next
                
                if current is not None:
                    result += ", "

                else:
                    result += "]"
                    print(result)
                    return True
        
        except Exception as err:
            print(err)
            return False


#   Adds the elements in otherList to this list.
#   Returns true if this list changed as a result of the call
    def addAll(self,otherList):
        initSize = self.getSize()

        for element in otherList:
            self.addLast(element)
        
        if self.getSize() > initSize:
            return True

        else:
            return False        
    

#   Removes all the elements in otherList from this list
#   Returns true if this list changed as a result of the call
    def removeAll(self,otherList):

        initSize = self.getSize()

        for selfElement in self:
            for otherElement in otherList:
            
                if self.indexOf(otherElement,self.getSize()) != -1:
                    self.removeAt(self.indexOf(otherElement,self.getSize()))
        
        if self.getSize() < initSize:
            return True

        else: 
            return False


#   Retains the elements in this list that are also in otherList
#   Returns true if this list changed as a result of the call
    def retainAll(self,otherList):

        initSize = self.getSize()
        newList = LinkList1()
        
        for selfElement in self:
            for otherElement in otherList:
                if selfElement == otherElement:
                    newList.add(selfElement)
        
        self.clear()
        
        for newElement in newList:
            self.add(newElement)  
        
        if self.getSize() < initSize:
            return True

        else: 
            return False
            

            
