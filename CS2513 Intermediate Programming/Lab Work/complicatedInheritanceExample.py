class Person:
	def display(self):
		print("Person called")
	
class Parent1(Person):
	pass
	
class Parent2(Person):
	def display(self):
		print("Parent2 called")
	
class Child(Parent1, Parent2):
	pass
	
child_obj = Child()
child_obj.display()

print(Child.__mro__)