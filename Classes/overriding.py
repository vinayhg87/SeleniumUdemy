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

    def drive(self):  # overriding drive method from super class.
        super().drive()  # calling super class method
        print("Start driving from subclass")


obj = subclass()
obj.drive()
obj.start()
obj.stop()