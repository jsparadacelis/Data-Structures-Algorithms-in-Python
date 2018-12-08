"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    """ **** Here is my code **** """
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        cont = 1
        current = self.head
        # mientras el contador es menor a la posición y haya nodo siguiente
        while(cont < position) and current.next:
            #nodo actual es igual a su nodo siguiente
            current = current.next
            cont+=1
        #Cuando el contador alcanza el valor de position
        if cont == position:
            #Retorna el nodo actual
            return current
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        #Obtiene el nodo anterior al de position
        before_element = self.get_position(position - 1)
        #next del nuevo nodo apuntará al next del nodo anterior
        new_element.next = before_element.next
        #El next del nodo anterior apuntará al nuevo nodo
        before_element.next = new_element
    
    def delete(self, value):
        """Delete the first node with a given value."""
        cont = 0
        current = self.head

        #Mientras el valor del nodo actual sea diferente
        while current.value != value and current.next:
            #Avanza sobre los nodos de la lista y aumenta el contador
            current = current.next
            cont += 1
        #si el nodo actual es la cabeza, reasigna la cabeza a su siguiente
        if current == self.head:
            self.head = current.next
        #si no es la cabeza
        else:
            #Encuentras su nodo anterior
            before_current = self.get_position(cont)
            #Reasigna el nodo siguiente del nodo anterior
            before_current.next = current.next
        #Apunta el siguiente a None (null)
        current.next = None
    
    

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value