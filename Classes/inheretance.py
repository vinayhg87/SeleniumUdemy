# in Python, there are only two types of Inheritance. Multiple Inheritance and Multilevel Inheritance.

class SuperClass(object):
    def __init__(self):
        print("From superclass constructor")

    def start(self):
        print("invoke Driving")

    def drive(self):
        print("Start Driving from super class")

    def stop(self):
        print("invoke Stop")


class subclass(SuperClass):
    def __init__(self):
        print("from subclass constructor")
        SuperClass.__init__(self)



obj = subclass()
obj.drive()
obj.start()
obj.stop()