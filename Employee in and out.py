class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")
def Create_obj():
    print("Object Created...")
    obj=Employee()
    print("Object Destructed...")
    del obj
obj=Create_obj()
print("Program ended")