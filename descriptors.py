Python descriptors or, more generally, descriptors provide you a powerful
technique to write reusable code that can be shared between classes.
They might seem similar to the concept of inheritance, but technically they are not.
They are a general-purpose way of intercepting attribute access.



To put it simply, a class that implements
__get__(), __set()__, or __delete()__ method for an object is known as a "Descriptor". 



The descriptors can be further categorized into data and non-data descriptors.
If the descriptor that you write has only __get__() method, then it is a non-data descriptor, on the other hand, implementation involving __set__() and __delete__() methods is called a data descriptor.
The non-data descriptors are only readable while the data descriptors are both readable and writable.



__get__() accesses the attribute or when you want to extract some information. It returns the value of the attribute or raises the AttributeError exception if a requested attribute is not present.

__set__() is called in an attribute assignment operation that sets the value of an attribute. Returns nothing. But can raise the AttributeError exception.

__delete__() controls a delete operation, i.e., when you would want to delete the attribute from an object. Returns nothing.


class DescriptorExample:
    """
    A descriptor which overrides the getting the setting 
    behaviour of the class attribute attached to it 
    """
    def __set__(self, instance, value):
        print(f"setting the value to {value}")

    def __get__(self, instance, owner):
        print(f"getting the value of the object's attribute")


class YourClass:
    """
    Attaching some_attr to the descriptor we just made
    Setting a value of some_attr or retrieving its value will 
    call __set__ and __get__ of the DescriptorExample
    """
    some_attr = DescriptorExample()

    def __init__(self, some_attr):
        self.some_attr = some_attr


your_class_obj = YourClass(5)


The output of the following code will be:
setting the value to 5




https://www.datacamp.com/community/tutorials/python-descriptors
https://medium.com/swlh/python-descriptors-a-practical-guide-to-solve-problems-using-reusable-code-fb98c68d1486