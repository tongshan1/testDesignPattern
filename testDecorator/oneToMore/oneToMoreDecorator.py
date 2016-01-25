__author__ = 'tongshan'

class mylocker:

    def __init__(self):
        print("mylocker.__init__() is called")

    @staticmethod
    def acquier():
        print("mylocker.acquier() is called")

    @staticmethod
    def unlock():
        print("mylocker.unlock() is called")


class lockerex(mylocker):

    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("  lockerex.unlock() called.")


def lockhelper(cls):

    """
    cls 必须实现acquire和unlock静态方法
    :param cls:
    :return:
    """
    def _deco(func):

        def __deco(*args,**kwargs):

            print("before %s called" % func.__name__)

            cls.acquier()

            try:
                return func(*args,**kwargs)
            finally:
                cls.unlock()
        return __deco

    return _deco

