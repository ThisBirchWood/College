from functools import total_ordering

@total_ordering
class TestClass:
    """ Represents an arbitrary thing, for testing the BST.

    BSTs require an ordering on the items that they store. Therefore, we
    need to make sure that any pair of instances can be compared to check
    whether one is 'less than' the other. Also, the standard definition of
    BSTs assume that if two instances are considered to represent the same
    thing, then only one of them is stored in the BST. Therefore, we need to
    specify how to compare two items. We specify methods for 'less than'
    (__lt__(...)) and 'equals' (__eq__(...)), and then the '@total_ordering'
    labelling above instructs Python to create the corresponding meaning of
    'greater than', 'less than or equal to', 'not equals', and so on. We can
    then use the standard comparison operators '==', '!=', '<', '<=', '>', '>='
    in our code when we need to compare two objects.

    In this TestClass, we say that two objects are equal if their values for
    'field1' are equal, and we say object1 is 'less than' the object2 if the
    value for object1.field1 < object2.field1.
    """

    def __init__(self, field1, field2=None):
        """ Initialise an object. """
        self._field1 = field1
        self._field2 = field2

    def __str__(self):
        """ Return a short string representation of this object. """
        outstr = self._field1
        return outstr

    def full_str(self):
        """ Return a full string representation of this object. """
        outstr = self._field1 + ": "
        outstr = outstr + str(self._field2)
        return outstr

    def __eq__(self, other):
        """ Return True if this object has exactly same field1 as other. """
        if (other._field1 == self._field1):
            return True
        return False

    def __lt__(self, other):
        """ Return True if this object is ordered before other.

        A thing is less than another if its field1 is alphabetically before.
        """
        if other._field1 > self._field1:
            return True
        return False



class BSTNode:
    """ An internal node for a Binary Search Tree.

    This gives a recursive definition of a BST, which consists of this node
    and all of its descendants. It allows us to implement recursive methods -
    e.g. to search a tree, we search at the root of the tree; if the element
    is there, we stop and return the value; if not, then we decide whether to
    go left or right, and then call the same search method on the appropriate
    child.

    Remember that if your recursive method ever returns anything, then it must
    return an appropriate value on every possible path through the method.

    Note that this assumes we can compare the relative ordering of any two
    items we want to add to the BST. That means there needs to be a definition
    of al least 'less than'and 'equals'. See the example of TestClass above.
    """
    
    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

        The string will be created by an in-order traversal.
        """
        outstr = ''
        if self._leftchild:
            outstr += '(' + str(self._leftchild)
        outstr += " " + str(self._element) + " "
        if self._rightchild:
            outstr += str(self._rightchild) + ')'

        return outstr

    def _stats(self):
        """ Return the basic stats on the tree rooted at this node. """
        return ('size = ' + str(self.size())
               + '; height = ' + str(self.height()))
    
  
    def search(self, searchitem):
        """ Return object matching searchitem, or None.

        That is, if an object matching searchitem appears anywhere in this
        node or in the subtree below it, then that object should be returned.

        Args:
            searchitem: an object of any class stored in the BST

        """
        return self.search_node(searchitem)._element
        

    def search_node(self, searchitem):
        """ Return the BSTNode (with subtree) containing searchitem, or None.

        That is, if an object matching searchitem appears anywhere in this
        node or in the subtree below it, then the BST node that points directly
        to that object should be returned.

        Args:
            searchitem: an object of any class stored in the BST
        """
        if self._element == searchitem:
            return self
        
        if searchitem < self._element:
            if self._leftchild is None:
                return None
            return self._leftchild.search_node(searchitem)
        elif searchitem > self._element:
            if self._rightchild is None:
                return None
            return self._rightchild.search_node(searchitem)

    def add(self, obj):
        """ Add item to the tree rooted at this node, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        if obj == self._element:
            return None
        
        if obj < self._element:
            if self._leftchild is None:
                self._leftchild = BSTNode(obj)
                self._leftchild._parent = self
            else:
                self._leftchild.add(obj)
        elif obj > self._element:
            if self._rightchild is None:
                self._rightchild = BSTNode(obj)
                self._rightchild._parent = self
            else:
                self._rightchild.add(obj)

        return obj
        
    def findmaxnode(self):
        """ Return the BSTNode with maximal element at or below here. """
        # method body goes here
        if self._rightchild is None:
            return self
        else:
            return self._rightchild.findmaxnode()
    
    def height(self):
        """ Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """

        if self.leaf():
            return 1
        elif self._leftchild and self._rightchild:
            return 1 + max(self._leftchild.height(), self._rightchild.height())
        elif self._leftchild:
            return 1 + self._leftchild.height()
        elif self._rightchild:
            return 1 + self._rightchild.height()

    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree, 
        including this node.
        """
        size = 1
        if self._leftchild:
            size += self._leftchild.size()
        if self._rightchild:
            size += self._rightchild.size()

        return size

    def leaf(self):
        """ Return True if this node has no children. """
        if self._leftchild or self._rightchild:
            return False
        return True

    def semileaf(self):
        """ Return True if this node has exactly one child. """
        if self._leftchild and self._rightchild:
            return False
        elif self._leftchild or self._rightchild:
            return True
        return False

    def full(self):
        """ Return true if this node has two children. """
        return (self._leftchild and self._rightchild)

    def internal(self):
        """ Return True if this node has at least one child. """
        if self._leftchild or self._rightchild:
            return True
        return False

    def remove(self, searchitem):
        """ Remove and return the object matching searchitem, if in this tree.

        Args:
            searchitem - an object of any class stored in the BST

        Remove the matching object from the tree rooted at this node.
        Maintains the BST properties.
        """
        item = self.search_node(searchitem)
        item.remove_node()
            
    def remove_node(self):
        """ Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
        #if this is a full node
            #find the biggest item in the left tree
            #  - there must be a left tree, since this is a full node
            #  - the node for that item can have no right children
            #move that item up into this item
            #remove that old node, which is now a semileaf
            #return the original element
        #else if this has no children
            #find who the parent was
            #set the parent's appropriate child to None
            #wipe this node
            #return this node's element
        #else if this has no right child (but must have a left child)
            #shift leftchild value up into this node, and clean up
            #return the original element
        #else this has no left child (but must have a right child)
            #shift rightchild value up into this node, and clean up
            #return the original element

        # method body goes here
        if self.full():
            max_left_node = self._leftchild.findmaxnode()
            old_element = self._element
            self._element = max_left_node._element

            max_left_node = None
            return old_element
        elif self.leaf():
            if self._parent._element > self._element:
                self._parent._leftchild = None
            else:
                self._parent._rightchild = None
            
            return self._element
        elif self._rightchild == None:
            old_element = self._element
            self._element = self._leftchild._element
            self._leftchild = None
            return old_element
        elif self._leftchild == None:
            old_element = self._element
            self._element = self._rightchild._element
            self._rightchild = None
            return old_element

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        if self._isthisapropertree() == False:
            print("ERROR: this is not a proper Binary Search Tree. ++++++++++")
        outstr = str(self._element) + ' (hgt=' + str(self.height()) + ')['
        if self._leftchild is not None:
            outstr = outstr + "left: " + str(self._leftchild._element)
        else:
            outstr = outstr + 'left: *'
        if self._rightchild is not None:
            outstr = outstr + "; right: " + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '; right: *]'
        if self._parent is not None:
            outstr = outstr + ' -- parent: ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- parent: *'
        print(outstr)
        if self._leftchild is not None:
            self._leftchild._print_structure()
        if self._rightchild is not None:
            self._rightchild._print_structure()

    def _properBST(self):
        """ Return True if this is the root of a proper BST; False otherwise. 

        First checks that this is a proper tree (i.e. parent and child
        references all link up properly).

        Then checks that the tree obeys the BST property.
        """
        if not self._isthisapropertree():
            return False
        return self._BSTproperties()[0]

    def _BSTproperties(self):
        """ Return a tuple describing state of this node as root of a BST.

        Returns:
            (boolean, minvalue, maxvalue):
                boolean is True if it is a BST, and false otherwise
                minvalue is the lowest value in this subtree rooted at this node
                maxvalue is the highest value in this subtree rooted at this node
        """
        minvalue = self._element
        maxvalue = self._element
        if self._leftchild is not None:
            leftstate = self._leftchild._BSTproperties()
            if not leftstate[0] or leftstate[2] > self._element:
                return (False,None,None)
            minvalue = leftstate[1]

        if self._rightchild is not None:
            rightstate = self._rightchild._BSTproperties()
            if not rightstate[0] or rightstate[1] < self._element:
                return (False,None,None)
            maxvalue = rightstate[2]

        return (True, minvalue,maxvalue)

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree.

        That is, it checks whether this node and its parents and children are
        all properly linked, and that the subtrees rotted at each child are
        also proper trees.
        """
        ok = True
        if self._leftchild is not None:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild is not None:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False          
        if self._parent is not None:
            if (self._parent._leftchild != self
                and self._parent._rightchild != self):
                ok = False
        return ok

def testadd():
    # creating five test objects to add to the tree
    mementoObj = TestClass("Memento", "11/10/2000")
    melvinObj = TestClass("Melvin and Howard", "19/09/1980")
    melvinObj2 = TestClass("Melvin and Howard", "21/03/2007")
    mellowObj = TestClass("Mellow Mud", "21/09/2016")
    melodyObj = TestClass("Melody", "21/03/2007")

    node = BSTNode(mementoObj)  # creating an initial BSTNode - a tree of size 1
    node._print_structure()

    # now adding something else to the tree, by calling add(...) on the root node
    print('> adding Melvin and Howard')
    node.add(melvinObj)
    node._print_structure()

    # now trying to add another object, but the definition of TestClass says
    # that if two instances have the same value for 'field1' then they are
    # considered to be equivalent, and so in this case, because they both have
    # field1 == "Melvin and Howard", the attempted addition should eventually
    # be rejected
    print('> adding a second version of Melvin and Howard - should fail')
    node.add(melvinObj2)
    node._print_structure()

    # now adding another item, again calling add(...) on the root node
    print('> adding Mellow Mud')
    node.add(mellowObj)
    node._print_structure()

    # now adding another item, again calling add(...) on the root node
    print('> adding Melody')
    node.add(melodyObj)
    node._print_structure()

    return node  # return the root, so you could use it at the command line

def test():
    node = BSTNode(TestClass("B", "b"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "A")
    node.add(TestClass("A", "a"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "A")
    node.remove(TestClass("A"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "C")
    node.add(TestClass("C", "c"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "C")
    node.remove(TestClass("C"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "F")
    node.add(TestClass("F", "f"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "B")
    node.remove(TestClass("B"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "C")
    node.add(TestClass("C", "c"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "D")
    node.add(TestClass("D", "d"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "C")
    node.add(TestClass("C", "c"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "E")
    node.add(TestClass("E", "e"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "B")
    node.remove(TestClass("B"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "D")
    node.remove(TestClass("D"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "C")
    node.remove(TestClass("C"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "E")
    node.remove(TestClass("E"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "L")
    node.add(TestClass("L", "l"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "H")
    node.add(TestClass("H", "h"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "I")
    node.add(TestClass("I", "i"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "G")
    node.add(TestClass("G", "g"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "L")
    node.remove(TestClass("L"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "H")
    node.remove(TestClass("H"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "I")
    node.remove(TestClass("I"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "G")
    node.remove(TestClass("G"))
    print('Ordered:', node)
    node._print_structure()
    print(node)


def me_test():
    node = BSTNode(17)
    node.add(5)
    node.add(4)
    node.add(5)
    node.add(35)
    node.add(25)
    node.add(39)
    node.add(12)
    node.add(11)
    node.add(428)
    node.remove(35)
    node.remove(39)
    print(node)


#testadd()
##print('++++++++++')
#test()

            
me_test()