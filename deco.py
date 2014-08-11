__author__ = 'Administrator'
# def deco(func):
#     print ("before myfunc() called")
#     func()
#     print ("after myfunc() called")
#     return func
def deco(arg):
    def _deco(func):
        def __deco():
            print ("before %s called %s") % (func.__name__,arg)
            func()
            print ("after %s called %s") % (func.__name__,arg)
        return __deco
    return _deco
@deco('aa')
def myfunc():
    print ("myfunc() called")
@deco('a2')
def myfunc2():
    print ("myfunc() called")
myfunc()
myfunc2()