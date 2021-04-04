getattr
__getattr__
__get__



getattr
getattr (object, name[, default])Is one of Python's built-in functions, its role is to get the properties of the object.

 - Object object
 - Name attribute name
 - Default The default value returned when the property does not exist
Example:

>>> class Foo:
...     def __init__(self, x):
...         self.x = x
...
>>> f = Foo(10)
>>> getattr(f, 'x')
10
>>> f.x
10
>>> getattr(f, 'y', 'bar')
'bar'




_ __getattr _ __
object. __getattr__(self, name)Is an object method that is called if the object's properties are not found.

This method should return the property value or throwAttributeErrorabnormal.

Note that if the object property can be found through the normal mechanism, it will not be called.__getattr__method.

Example:

>>> class Frob:
...     def __init__(self, bamf):
...         self.bamf = bamf
...     def __getattr__(self, name):
...         return 'Frob does not have `{}` attribute.'.format(str(name))
...
>>> f = Frob("bamf")
>>> f.bar
'Frob does not have `bar` attribute.'
>>> f.bamf
'bamf'




 __ get __
__get__()The method is one of the descriptor methods. Descriptors are used to transform access object properties into call descriptor methods.

Example:

class Descriptor(object):
    def __get__(self, obj, objtype):
        print "get value=%s" % self.val 
        return self.val
 
    def __set__(self, obj, val):
        print "set value=%s" % val
        self.val = val
 
class Stu(object):
    age = Descriptor()
 
stu = Stu()
stu.age = 12    # set value=12
print stu.age   # get value=12





https://www.programmersought.com/article/2708863685/