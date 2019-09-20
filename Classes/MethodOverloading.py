# In Python, overloading is not an applied concept.
# we need to use a package like pythonlangutil to get the method overloading functionality or use the below technique.
# None is a keyword which is equivalent to null.
# Python does not support method overloading, that is, it is not possible to define more than one method with the same name in a class in python.
# This is because method arguments in python do not have a type.


class methodOverLoading(object):

    def test1(self, input1=None, input2 = None):

        if input1 is not None and input2 is not None:
            print("from test1(input1, input2) %s" % str(input1))
        else:
            print("from no arg method")


obj = methodOverLoading()
obj.test1("hello", "hello2")
obj.test1()
