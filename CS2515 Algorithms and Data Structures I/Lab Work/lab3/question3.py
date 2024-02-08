from stackA import Stack
from time import perf_counter

def reverse_stack(stack):
    reverse_stack = Stack()

    while stack.length() > 0:
        reverse_stack.push(stack.pop())

    return reverse_stack


#example: 24, 25, 73 ,[24, 52, 73, 2], {2436, 25, 24}, 242, 25, 84, 23
brackets = [("[", "]"), ("(", ")"), ("{", "}")]
open_brackets_conversion = {"[": "]", "(": ")", "{": "}"}
def check_string(string):
    open_brackets_stack = Stack()
    
    for char in string:
        if char in [x[0] for x in brackets]:
            open_brackets_stack.push(char)
        elif char in [x[1] for x in brackets]:
            last_bracket = open_brackets_stack.top()

            if open_brackets_conversion[last_bracket] == char:
                open_brackets_stack.pop()
            else:
                return False
    
    if open_brackets_stack.length() == 0:
        return True
    return False

n = 1000000
string = ''
for i in range(n):
    string += "("
for i in range(n):
    string += ")"
start_time = perf_counter()
print(check_string(string))
end_time = perf_counter()
print('{:.30f}'.format(end_time - start_time))