import random, time
from stackA import Stack

colours = {0: 'green', 1: 'red', 2: 'blue'}

def tetris1():
    blocks = []
    stack = Stack()
    points = 0
    
    for i in range(25):
        blocks.append(random.randint(0, 2))

    for block in blocks:
        print("-------------")
        print(f"Your block: {colours[block]}")

        start_time = time.time()
        user_input = input("Accept/reject? (y/n) ")
        end_time = time.time()
        time_to_ans = end_time - start_time

        if user_input == "y" and time_to_ans < 4:
            if stack.top() == block:
                stack.pop()
                print("Two matched! +1 point")
                points += 1
            else:
                stack.push(block)
        elif time_to_ans >= 4:
            stack.push(block)
            print("You took too long! Block added!")
        else:
            stack.push(block)

    points -= stack.length()
    print(f"You got {points} points!")

def tetris2(stack_amount, height, rounds):
    blocks = []
    stacks = []
    points = 0
    
    for i in range(stack_amount):
        stacks.append(Stack())

    for i in range(rounds):
        blocks.append(random.randint(0, 2))

    for block in blocks:
        print("-------------")
        print(f"Your block: {colours[block]}")

        start_time = time.time()
        user_input = int(input(f"Which stack append to? (1-{stack_amount}) ")) - 1
        end_time = time.time()
        time_to_ans = end_time - start_time

        if stacks[user_input].top() == block:
            stacks[user_input].pop()
            print("+1 Point")
            points += 1
        elif time_to_ans > 4:
            print("You took too long! The block has been added to Stack 1!")
            stacks[0].push(block)
        else:
            stacks[user_input].push(block)

        if stacks[user_input].length() >= height:
            print(f"You lose! Stack {user_input+1} is full!")
            return
        
    print(f"You got {points} points!")

tetris2(5, 10, 20)