'''
    Richard Elgar
    SDEV220
    Implemenet set operations in LinkedList


Modify LinkedList to implement the following set methods:

    def addAll(self, otherList):

    def removeAll(self, otherList):

    def retainAll(self, otherList):
'''


#   -------------------------------------------------------------------
#           ORIGINAL LINKEDLIST & NODE CLASSES/FUNCTIONS
#   -------------------------------------------------------------------

# The Node class
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedListIterator: 
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element    


class LinkList1:
#   class constructor; initialize head and tail attributes to 'None', size to '0'
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0


# Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.__head # link the new node with the head
        self.__head = newNode # head points to the new node
        self.__size += 1 # Increase list size

        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):
        if e is not Node:
            newNode = Node(e) # Create a new node for e
    
        if self.__tail == None:
            self.__head = self.__tail = newNode # The only node in list
        else:
            self.__tail.next = newNode # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
    
        self.__size += 1 # Increase size

    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self.__size:
            self.addLast(e) # Insert last
        else: # Insert in the middle
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def removeFirst(self):
        if self.__size == 0:
            return None # Nothing to delete
        else:
            temp = self.__head # Keep the first node temporarily
            self.__head = self.__head.next # Move head to point the next node
            self.__size -= 1 # Reduce size by 1
            if self.__head == None: 
                self.__tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None # Nothing to remove
        elif self.__size == 1: # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head
        
            for i in range(self.__size - 2):
                current = current.next
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

#   Remove the element at the specified position in this list.
#   Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next
        
                current = previous.next
                previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
    
    # Return the size of the list
    def getSize(self):
        return self.__size


#   ---------------------------------------
    def __str__(self):
        
        #if self.getSize() == 1:
         #   return -1
        
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result
#   -----------------------------------------


    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)
    
    
    
    
#   -------------------------------------------------------------------
#                       IMPLEMENTED FUNCTIONS
#   -------------------------------------------------------------------    
    

#   returns the index of the first occurence of a value in a LinkList1 instance; if the value is not found, returns -1 
    def indexOf(self,e,listLength):
        result = 0
        if listLength <= 0:
            return -1

        for node in self:
            
            if node == e:
                return result
            
            else:
                node = Node(node)
                if node.next == None:
                    return -1
                else:
                    result += 1
            
        return -1
    

#
    def addNodeLast(self,node):
        try:
            if node is Node:
                
                if self.__tail == None:
                    self.__head == self.__tail == node
                    return True
                    
                else:
                    self.__tail.next == node
                    self.__tail = self.__tail.next
                    return True
            
            else: return False
        
        except Exception as nodeErr:
            print("\n--------------------------------\n\t\tERR::addNodeLast()\n--------------------------------\n",nodeErr,\
                "\n\n--------------------------------\n--------------------------------")
            
            


#   Adds the elements in otherList to this list.
#   Returns true if this list changed as a result of the call
    def addAll(self,otherList):
        try:
            initSize = self.getSize()

            for node in otherList:
                if type(node) is not Node:
                    raise Exception("NOT NODE EXCEPTION")
                    
                self.addLast(node)
            
            if self.getSize() > initSize:
                return True

            else:
                return False        
        
        except Exception as err:
            print(err)
            
            
    

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

    
    def printOutputStr(self):
        if self.__head.element is None:
            return "LinkedList is empty"
        
        result = "["
        current = self.__head

        for i in range(self.__size):
            result += current.element
            if current.next is not None:
                result += ", "
                current = current.next
            
            else: result += "]"
        
        return result
        