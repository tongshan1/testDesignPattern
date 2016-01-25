__author__ = 'tongshan'

def deco(arg):

    def _deco(func):

        def __deco():

            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("after %s called." % func.__name__)

        return __deco
    return _deco

@deco("myModule")
def myfunc():
    print("myfunc() called.")

@deco("myModule1")
def myfunc1():
    print("myfunc() called.")


if __name__ == "__main__":
    myfunc()
    myfunc1()
