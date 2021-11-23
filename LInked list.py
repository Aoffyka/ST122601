import random
import time

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__ (self): 
    	self.head = None
    def append(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=temp  

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data + " -> ", end="")
            temp = temp.next

    def searchList(self):
            plate = str(input("Enter plate to search: "))
            t0 = time.perf_counter()
            print(self._searchList(plate))
            t1 = time.perf_counter()
            print("Time:", t1 - t0)
            
    def _searchList(self,plate):
        temp = self.head
        while (temp):
            if temp.data == plate:
                return "Plate is found"
            temp = temp.next
        return "Plate is not found"   

    def deleteNode(self):
            plate = str(input("Enter plate to delete: "))
            t0 = time.perf_counter()
            self._deleteNode(plate)
            t1 = time.perf_counter()
            print("Time:", t1 - t0)

    def _deleteNode(self, key):   
        # Store head node
        temp = self.head
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None

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
        for i in range(0,numplate):
            self.append(thai_plate[i])
        return thai_plate 

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

    def generateNewPlate(self):
        temp = str(input("Enter New plate: "))
        if self._searchList(temp) == "Plate is found":
            print("Plate is already exist, please try again")
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
ch = 1
list = LinkedList()
list.start_numplate()
print(list.printList())
while ch in (1, 2, 3, 4, 5):
    ch = list.menu()
    if ch == 1:
        newPlate = list.generateNewPlate()
        if newPlate:
            list.append(newPlate)
    elif ch == 2:
        list.searchList()
    elif ch == 3:
        print(list.printList())
    elif ch == 4:
        sp = list.deleteNode()
    elif ch == 5:
        print("Thank you for using generate random plate.")
        for val in range(0, 5):
            if val == 3:
                print(exit)
                exit()
            print(val+1)
    else:
        ch = list.menu()                    