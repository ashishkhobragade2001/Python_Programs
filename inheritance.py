class Parent():
    def __init__(self, name):
        self.name = name 
    
    def my_age(self, age):
        print(f"my name is {self.name}, and age is {age}")
        
class Child(Parent):
    def __init__(self, name, child_name):
        super().__init__(name)
        self.child_name = child_name
    
    def Child_add(self, add):
        print(f"My parent name is {self.name}, and my name is {self.child_name}, and I am from {add}")
obj_parent = Parent("Ashish")
obj_parent.my_age("30")

obj_child = Child("Ashish", "Shaurya")
obj_child.Child_add("Yavatmal")
