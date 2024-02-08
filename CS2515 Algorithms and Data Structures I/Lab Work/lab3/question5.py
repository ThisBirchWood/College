from stackA import Stack
brackets = []
operators = {'*': 1, "/": 1, "+": 2, "-": 2}

def infix_to_postfix(expression):
    stack = Stack()
    numbers = []

    for char in expression:
        if char.isdigit():
            numbers.append(int(char))
        elif char == "(":
            stack.push(char)
        elif char in operators.keys():
            precedence_current_char = operators[char]
            
            if stack.top() in operators.keys():
                precedence_last_operater = operators[stack.top()]

                if precedence_last_operater <= precedence_current_char:
                    numbers.append(stack.pop())
            stack.push(char)

        elif char == ")":
            while stack.top() != "(":
                numbers.append(stack.pop())
            stack.pop()

    while stack.length() > 0:
        numbers.append(stack.pop())

    return_string = ''
    for char in numbers:
        return_string += str(char)
        return_string += " "

    return return_string

print(infix_to_postfix("(7 + 8 / 4) / 3 * 5"))
        
        