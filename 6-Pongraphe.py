"""
The stact is a collection of items that follows the LAST-in, First-out data structure.

For the addintion of new items, the stack only allows it to push the new item to
the top. When it comes to removing items, it only allows us to remove the last
added item or called the top item.

By using "push" (ADD) , "pop" (REMOVE).
REF:https://medium.com/the-renaissance-developer/stack-data-structure-f8da15cb4c12
"""

class Stack:
    
    def __init__(self):
        self.items = []  #items list to store the stack items.

    def push(self, item):
        self.items.append(item) # To receives the new item

    def size(self):
        return len(self.items)

    def is_empty(self): # TO verify whether the list has items or not. 
        return self.size() == 0

    def pop(self):
        if self.is_empty():
            raise Emptiness('The stack is empty')
        
        return self.items.pop()
    
    def top(self):
        if self.is_empty():
            raise Emptiness('The Stack is empty')
        return self.items[-1]
    
class Emptiness(Exception):
    pass

open_list = ["(","[","{"]
close_list = [")","]","}"]

def checkValueInput(s):
    stack = Stack()
    for i in s:
        if i in open_list:
            stack.push(i)
            #print(stack,i)
            #print(stack.size())
        elif i in close_list:
            #print(stack,i)
            if (stack.size() > 0):
                if stack.top() == '[' and i == ']':
                    stack.pop()
                elif stack.top() == '(' and i == ')':
                    stack.pop()
                elif stack.top() == '{' and i == '}':
                    stack.pop()
                else:
                    pass
            else:
                print("Not Ok")
    if stack.is_empty():
        print("OK")
    else:
        print("Not OK")

print("------- TESTING STACK --------")
#checkValueInput("{[[]]{()}}")
#checkValueInput("[{({([[[[)}}}]]")
#checkValueInput("[({})]{()}")
checkValueInput("[]{}()")


