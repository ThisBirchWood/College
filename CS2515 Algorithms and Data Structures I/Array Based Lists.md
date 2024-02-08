# Arrays
- Arrays are blocks of memory of a fixed size, which is determined when it's created
- Cells within the array must be of a fixed size, otherwise the program won't know when the next element begins
![[Pasted image 20231003192754.png]]
- Address of cell i = Address of Cell 0 + (i * size)


# Python Memory Management
## Variables
- Take the following code:
```
x = 3
y = 3
z = y
y = 4
```
- 3 is an integer object, stored in memory
- x is a variable which references/points to that object
- y is a variable which references/points to the very same object
- z is a variable which references/points to the very same object
- y is then changed to point to a different integer object (4)
![[Pasted image 20231003193454.png]]

## User defined Objects
- Every time an instance of a class is initialised, Python stores the new object in memory

```
c1 = Card(3, 3)
c2 = Card(3, 3)     #same values, though a different object in memory
c3 = c2
c2 = Card(6, 1)
```
![[Pasted image 20231003193833.png]]

## Lists
- A list in Python is just an array, however instead of storing the object itself in the array, it stores the **reference** to the object.
- This is the reason Python can store multiple data types in the same list.
![[Pasted image 20231003194122.png]]

### Space required for a list
- Since a python list is an array of references, the amount of memory it takes up depends on the length of the list alone, with the data within the cells of the list not making any difference
```
listA = [1,2,3,4,5,6,7,8,9]     #length of 9 elements
listB = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]        #length of nine elements
```
- Both lists in this code take up the same amount of bytes in memory

### Increasing list size
- If the array has data after it, then the computer needs to move the entire list to the front of the memory
- This can be very resource intensive and time consuming and should generally be avoided, due to the fact it has to copy the whole list every time an element is added
![[Pasted image 20231004000341.png]]
- Python optimizes this by creating a bigger array space than is needed initially
 ![[Pasted image 20231004000819.png]]
 
## Tuples
- Tuples are similar to lists, except for the fact that they are immutable (unchangeable)
- The length and content of a tuple cannot change
- The main difference between an array and a tuple, is that tuples can store multiple data types
