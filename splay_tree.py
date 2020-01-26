__GroupMembers = {'Asma Hai':'18B-013-CS-A',
                    'Zarar Ali Shah':'18B-075-CS-A',
                    'Kainat Khurshid':'18B-014-CS-A'}
print("\n<<------ GROUP MEMBERS ------>>\n")
for keys in __GroupMembers:
    print(">> {} \t\t\t {}".format(keys , __GroupMembers[keys]))
print()
print("Data Structures and Algorithm\nSemester III - Project\nTopic : \t\t\t\t\t''' Splay Tree '''")
print()
print()
print()

# first we will create a Node class in which we are inputting value
# parent pointer is for splaying , indentification of the right rotation
# right side of tree stores the values greater than the root node
# left side of tree stores the values less than the root node

# as python programming language doesnt have pointers hence
# we will be using wrapper functions 'def __<functionname>()'
# as the user is unaware of the root node

class Node:
    def __init__(self , value):
        self.value = value
        self.parent = None      # for splaying
        self.right = None
        self.left = None

class SplayTree:
    def __init__(self):
        self.root = None    # root node

    # left rotation is called 'Zag Rotation'
    # Zag rotation on parent node
    # if the node itself is root node then no rotation needed
    def __leftrotation(self , x):   # left rotation at node 'x'
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # right rotation is called 'Zig Rotation'
    # Zig rotation on parent node
    # if the node itself is root node then no rotation needed
    def __rightrotation(self, x):       # right rotation at node 'x'
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y


    """ Splaying - it is basically bringing the required node to the root of the tree
    through series of rotations on the tree because of this splaying property the cost or running time of sply tree is good
    as the most accessed node comes near to the root node due to continous splaying .
    In splaying different rotations are decided by considering the parent node """

    def __splay(self , n):
        # if n.parent == None - the no splaying is needed as the node is already the root node
        while n.parent != None: # means the the node is not the root node as it has parent node
            if n.parent.parent == None: # means that the node has only 1 parent which is the root node
                if n == n.parent.left:
                    # Case 1 : Zig Rotation
                    # when node has 1 parent only which makes it the root node
                    self.__rightrotation(n.parent)
                else:
                    # Case 2 : Zag Rotation ( left rotation )
                    # when node has 1 parent only which makes it the root node
                    self.__leftrotation(n.parent)

            # Case 3 : Zig-Zig Rotation ( 2 right rotations)
            # when there is twice zig rotation first rotation is on grandparent and
            # second is on the parent
            elif n == n.parent.left and n.parent == n.parent.parent.left:
                # right rotation on grandparent
                self.__rightrotation(n.parent.parent)
                # right rotation on parent
                self.__rightrotation(n.parent)

            # Case 4 : Zag-Zag Rotation  ( 2 left rotations )
            elif n == n.parent.right and n.parent == n.parent.parent.right:
                # left rotation on grandparent
                self.__leftrotation(n.parent.parent)
                # left rotation on parent
                self.__leftrotation(n.parent)

            # Case 5 : Zag-Zig rotation
            # first left rotation on parent and then right rotation
            elif n == n.parent.right and n.parent == n.parent.parent.left:
                self.__leftrotation(n.parent)
                self.__rightrotation(n.parent)

            # Case 6 : Zig-Zag rotation
            # first right rotation on parent and then left rotation
            elif n == n.parent.left and n.parent == n.parent.parent.right:
                self.__rightrotation(n.parent)
                self.__leftrotation(n.parent)

    '''<<<<< --------------------- Function no . 1 - SEARCH node in tree --------------------- >>>>>'''
    def Search(self , value):
        search = self.__Search(self.root , value)
        if search != None:
            self.__splay(search)

    def __Search(self , temp , value):
        '''case 1 : --> tree is empty returns none
                    --> the node to be searched is already the root hence complexity is O( 1 ) '''
        # temp <-- self.root
        if temp == None or value == temp.value:
            return temp
        '''case 2 : normal BST searching 
                    --> if node < self.root(temp) than return root.left
                    --> if node > self.root(temp) than return root.right'''

        if value < temp.value:
            return self.__Search(temp.left ,value )
        return self.__Search(temp.right , value)



    '''<<<<< --------------------- Function no . 2 - INSERT node in tree --------------------- >>>>>'''
    def Insert(self , value):
        self.__Insert(self.root , value)

    def __Insert(self ,temp, value):
        '''temp is a pointer variable and "a" will contain the addresses of nodes '''
        n = Node(value)
        #temp = self.root
        a = None    # second pointer
        '''self.root not none means the node has parent '''
        while temp != None:
            a = temp        # pointer set to temp which is self.root
            '''Check if value < self.root insert in left tree else insert in right tree'''
            '''left subtree holds values less than root node while 
            right subtree holds greater values'''
            if n.value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        '''for a is parent of node 
        pointer a is on root node now '''
        n.parent = a
        '''if parent which is the root node is none'''
        if a == None:
            self.root = n  # insert node is set to root node as root node is none hence tree is empty
        # same conditions applied
        elif n.value < a.value:
            a.left = n

        else:
            a.right = n

        # now splaying the node - which is positioning newly inserted node to root node
        self.__splay(n)

    '''<<<<< --------------------- Function no . 3 - DELETE node in tree --------------------- >>>>>'''

    '''for deleting operation 
    -->> the node to be deleted is splayed and the deleted leaving two subtrees behind
    -->> left subtree - smaller values
    -->> right subtree - larger values
    the the left subtree is splayed such that its maximum value'''

    def Delete(self , key):
        self.__Delete(self.root , key)

    def __Delete(self ,temp,value):
        z = None    # as a pointer variable
        x = None    # tree 1 - subtree
        y = None    # tree 2 - subtree

        while temp != None:
            if temp.value == value:
                z = temp

            if temp.value >= value:
                temp = temp.left

            else:
                temp = temp.right


        # condition -- where the node to be deleted is not in the tree
        if z == None:
            print("Value not found !! ")

        # splitting the tree after deletion of the node

        x , y = self.__Split(z)

        # joining the subtrees by splaying maximum node of left subtree
        # left subtree's right child <-- NULL
        # right subtree's left child <-- NULL
        # hence joining right subtree to the right child of left subtree

        if y.left != None:
            y.left.parent = None

        self.root = self.__Join(y.left , x)
        y = None


    '''<<<<< ------------ JOIN Operation ------------- >>>>>'''

    # joining two trees or sub-trees(for delete function) x & y
    def __Join(self, s, t):
        # when tree - x is null so no join operation hence it returns the existing tree
        if s == None:
            return t

        # when tree - y is null so no join operation hence it returns the existing tree
        if t == None:
            return s

        # splaying maximum node of left subtree
        x = self.Maximum(s)        # extracting minimum node of left subtree
        self.__splay(x)
        x.right = t
        t.parent = x
        return x

    '''<<<<< ------------ SPLIT Operation ------------- >>>>>'''
    # we will splay the given parameter
    # left subtree is either small than the given parameter of equal to the given parameter
    # right subtree is greater than the parameter
    # hence the tree is splitted into two sub-trees
    # if parameter is equal to left subtree it will attach to left else right subtree

    def __Split(self , z):
        self.__splay(z)
        if z.right != None:
            x = z.right
            x.parent = None
        else:
            x = None

        y = z
        y.right = None
        z = None
        return x , y

    '''<<<<< ------------ MINIMUM & MAXIMUM nodes ------------- >>>>>'''
    
    # minimum element is the left-most leaf node of a tree
    def Minimum(self , node):
        while node.left != None:
            node = node.left
        return node

    # maximum element is the right-most leaf node of a tree
    def Maximum(self , node):
        while node.right != None:
            node = node.right
        return node

    '''<<<<< ------------ SUCCESSOR & PREDECESSOR ------------- >>>>>'''

    # successor of a node
    '''-->> Successor is the left-most in right subtree'''
    
    def Successor(self , node):
        # condition for checking if right subtree is not NULL
        if node.right != None:
            self.Minimum(node.right)

        x = node.parent
        while x != None and node == x.right:
            node = x
            x = x.parent
        return x


    # predecessor of a node
    '''-->> Predecessor is the right-most of the left subtree'''
    
    def Predecessor(self , node):
        if node.left != None:
            self.Maximum(node.left)

        x = node.parent
        while x != None and node == x.left:
            node = x
            x = x.parent
        return x

    '''<<<<< ------------ TREE TRAVERSAL ------------- >>>>>'''

    #  1. L (C) R -->  tree traversal
    # wrapper function
    
    def InOrder(self):
        return self.__InOrder_traverse(self.root)

    def __InOrder_traverse(self , node):
        if node != None:
            self.__InOrder_traverse(node.left)
            print(node.value)
            self.__InOrder_traverse(node.right)

    # 2 . (C) L R --> tree traversal
    # wrapper function
    
    def PreOrder(self):
        return self.__PreOrder_traverse(self.root)

    def __PreOrder_traverse(self , node):
        if node != None:
            print(node.value)
            self.__PreOrder_traverse(node.left)
            self.__PreOrder_traverse(node.right)

    # 3 . L R (C) --> tree traversal
    # wrapper function
    
    def PostOrder(self):
        return self.__PostOrder_traverse(self.root)

    def __PostOrder_traverse(self ,  node):
        if node != None:
            self.__PostOrder_traverse(node.left)
            self.__PostOrder_traverse(node.right)
            print(node.value)

    '''<<<<< ------------ PRINTING SPLAY TREE ------------- >>>>>'''

    # wrapper function
    def print_splaytree(self):
        # space=[0]
        # Pass initial space count as 0
        self.__print(self.root, 0)

    
    def __print(self,root, space):
        count = [10]    # counter for spacing
        if (root == None):
            return

        space += count[0]

        self.__print(root.right, space)     # right child

        print()
        
        for i in range(count[0], space):
            print(end=" ")
            
        print(root.value)                   # current

        self.__print(root.left, space)      # left child



if __name__ == "__main__":
  
    s = SplayTree()
    s.Insert(15)
    s.Insert(10)
    s.Insert(17)
    s.Insert(7)
    s.Insert(13)
    s.Insert(16)
    s.Insert(12)
    s.Insert(14)
    s.Insert(11)
    print("Inserting Nodes ....")
    s.print_splaytree()

    d = [11,16,14]
    for i in range(len(d)):
        print("\nDeleting {} ....\n".format(d[i]))
        s.Delete(d[i])
        s.print_splaytree()

    search = [10,15,13,12]
    for i in range(len(search)):
        print("\nSearching {} ....\n".format(search[i]))
        s.Search(search[i])
        s.print_splaytree()


