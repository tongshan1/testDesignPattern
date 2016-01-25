__author__ = 'tongshan'

from testDecorator.oneToMore.oneToMoreDecorator import *

class example:

    @lockhelper(mylocker)
    def myfunc1(self):
        print("my func called.")


    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc2(self, a, b):
        print("myfunc2() called")
        return (a+b)

if __name__ == "__main__":
    a = example()
    a.myfunc1()
    print(a.myfunc1())
    print(a.myfunc2(1, 2))
    print(a.myfunc2(3, 4))
