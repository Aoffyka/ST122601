# Source https://qvault.io/python/binary-search-tree-in-python/
import random
import time

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def generateNewPlate(self):
        temp = str(input("Enter New plate: "))
        if self.exists(temp):
            print("Plate is already exist, please try again")
            # Return to the menu 
            return ''
        elif not temp:
            print("Plate is empty, please try again") 
            return ''   
        elif len(temp) < 5:
            print("Invalid Input")
            return ''
        else:
            print("New plate:", temp)
            return temp

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)   

    def delete(self):
        val = str(input("Enter the plate you want to delete: "))
        self._delete(val)

    def _delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right # Find the min value in the right subtree
        while min_larger_node.left:
            min_larger_node = min_larger_node.left 
        self.val = min_larger_node.val # Replace the value of the current node with the min value in the right subtree
        self.right = self.right.delete(min_larger_node.val) 
        return self 

    def find(self):
        query = str(input("Please enter the plate you looking for: "))
        t0 = time.perf_counter()
        # Call 
        found = self.exists(query)
        t1 = time.perf_counter()
        print("S time", t0)
        print("E Time", t1)
        print("Time spent:",t1-t0) 
        if found:
            print("Plate is found")
        else:
            print("Plate is not found")

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)             

    def start_numplate(self):
    #Generate random plate
        numplate = int(input("Please enter amount of random plates: "))
        thai_plate = []
        char0 = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
        char1 = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
        char2=  '0123456789'
        len0 = len(char0) - 1
        len1 = len(char1) - 1
        len2 = len(char2) - 1
         # loop for the amount of plate user desire
        for i in range(0,numplate):
            code = ''
            index0 = random.randint(1,len0)
            index1 = random.randint(1,len1)
            code += char0[index0]
            code += char1[index1]
            # Loop for 4 digit code
            for i in range(0, 4):
                index2 = random.randint(0, len2)
                code += char2[index2]
            thai_plate.append(code)
        # To prevent creating sub-array using insert function  
        for i in range(0,numplate):
            self.insert(thai_plate[i])
        return thai_plate 
    # Using source from the internet. 
    def print_tree(root, val="val", left="left", right="right"):
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

        # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, val, left, right)
        for line in lines:
            print(line)
    #In-order 
    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals        
    # All Choices 
    def menu(self):
        print("\n\t\t\tThai license plate ")
        print("\tPlease select one of the below choices\n")
        print("1. Add a new plates")
        print("2. Search for a plate")
        print("3. Display all plate")
        print("4. Remove an existing plate")
        print("5. Exit Thai plate")
        choice = int(input("Please enter your choice: "))
        return choice        

ch = 1
bst = BSTNode()
bst.start_numplate()
# Sort In-order first 
print(bst.inorder([]))
while ch in (1, 2, 3, 4, 5):
    ch = bst.menu()
    if ch == 1:
        newPlate = bst.generateNewPlate()
        if newPlate:
            bst.insert(newPlate)
    elif ch == 2:
        bst.find()
    elif ch == 3:
        print("Display All the plate:\n ",bst.inorder([]))
        #bst.print_tree()
    elif ch == 4:
        sp = bst.prepareDelete()
    elif ch == 5:
        print("Thank you for using generate random plate.")
        for val in range(0, 5):
            if val == 3:
                print(exit)
                exit()
            print(val+1)
    else:
        ch = bst.menu()