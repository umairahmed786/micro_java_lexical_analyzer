import random




class RBNode:

    def __init__(self, val):

        self.red = False

        self.parent = None

        self.val = val

        self.left = None

        self.right = None

class RBTree:

    def __init__(self):

        self.nil = RBNode(0)

        self.nil.red = False

        self.nil.left = None

        self.nil.right = None

        self.root = self.nil

    def insert(self, val):

        # Ordinary Binary Search Insertion

        new_node = RBNode(val)

        new_node.parent = None

        new_node.left = self.nil

        new_node.right = self.nil

        new_node.red = True  # new node must be red

        parent = None

        current = self.root

        while current != self.nil:

            parent = current
            if len(new_node.val.lexeme) < len(current.val.lexeme):
                
                current = current.left
            elif len(new_node.val.lexeme) == len(current.val.lexeme):
                
                if new_node.val.lexeme < current.val.lexeme:

                    current = current.left

                else:

                    current = current.right
            elif len(new_node.val.lexeme) > len(current.val.lexeme):
                current = current.right
            else:

                return

        # Set the parent and insert the new node

        new_node.parent = parent

        if parent == None:

            self.root = new_node

        elif len(new_node.val.lexeme) < len(parent.val.lexeme):

            parent.left = new_node
        elif len(new_node.val.lexeme) == len(parent.val.lexeme):
            if new_node.val.lexeme < parent.val.lexeme:
                parent.left = new_node
            else:
                parent.right = new_node
        else:

            parent.right = new_node

        # Fix the tree

        self.fix_insert(new_node)

    def fix_insert(self, new_node):

        while new_node != self.root and new_node.parent.red:

            if new_node.parent == new_node.parent.parent.right:

                u = new_node.parent.parent.left  # uncle

                if u.red:

                    u.red = False

                    new_node.parent.red = False

                    new_node.parent.parent.red = True

                    new_node = new_node.parent.parent

                else:

                    if new_node == new_node.parent.left:

                        new_node = new_node.parent

                        self.rotate_right(new_node)

                    new_node.parent.red = False

                    new_node.parent.parent.red = True

                    self.rotate_left(new_node.parent.parent)

            else:

                u = new_node.parent.parent.right  # uncle



                if u.red:

                    u.red = False

                    new_node.parent.red = False

                    new_node.parent.parent.red = True

                    new_node = new_node.parent.parent

                else:

                    if new_node == new_node.parent.right:

                        new_node = new_node.parent

                        self.rotate_left(new_node)

                    new_node.parent.red = False

                    new_node.parent.parent.red = True

                    self.rotate_right(new_node.parent.parent)

        self.root.red = False

    def exists(self, val):

        curr = self.root

        while curr != self.nil and val.lexeme != curr.val.lexeme:

            if val.lexeme < curr.val.lexeme:

                curr = curr.left

            else:

                curr = curr.right

        
        return curr

    # rotate left at node x

    def rotate_left(self, x):

        y = x.right

        x.right = y.left

        if y.left != self.nil:

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

    # rotate right at node x

    def rotate_right(self, x):

        y = x.left

        x.left = y.right

        if y.right != self.nil:

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



    def __repr__(self):

        lines = []

        print_tree(self.root, lines)

        return '\n'.join(lines)

def print_tree(node, lines, level=0):

    if node.val != 0:

        print_tree(node.left, lines, level + 1)

        lines.append('-' * 4 * level + '> ' +

                     str(node.val.lexeme) + ' ' + ('RED NODE' if node.red else 'BLUE NODE'))

        print_tree(node.right, lines, level + 1)

def get_nums(num):

    random.seed(1)

    nums = []

    for _ in range(num):

        nums.append(random.randint(1, num-1))

    return nums
