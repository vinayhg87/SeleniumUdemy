

class TestClass(object):  # TestClass inherits the properties of Object class. (Same as Java)
    def __init__(self, make):  # This is a constructor.
        self.make = make    # self is like a 'this' keyword in Java. This points to the current instance.


obj1 = TestClass("BMW")
print(obj1.make)

obj2 = TestClass("BENZ")
print(obj2.make)
