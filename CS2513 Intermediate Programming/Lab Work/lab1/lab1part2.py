numbers = input("Enter 5 numbers (seperated with spaces): ").split(" ")
numbers = [int(x) for x in numbers]

sum = sum(numbers)
average = round(sum / len(numbers), 2)
print("Sum:", sum)
print("Average:", average)
