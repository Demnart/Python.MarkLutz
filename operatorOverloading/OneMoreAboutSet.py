
class PrivateException(Exception):
    pass

class Privacy:
    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivateException
        else:
            self.__dict__[key] = value
class Test1(Privacy):
    privates = ['age']
class Test2(Privacy):
    privates = ['age','pay']
    def __init__(self):