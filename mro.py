class BaseModule:
    module_name = "top"

    def __init__(self, module_name):
        self.name = module_name

    def __str__(self):
        return "{}:{}".format(self.module_name, self.name)
    

class BaseModule1(BaseModule):
    module_name = "module-1"


class BaseModule2(BaseModule):
    module_name = "module-2"


class BaseModule3(BaseModule):
    module_name = "module-3" 


class Module12(BaseModule1, BaseModule2):
    """extends 1 & 2"""


print(str(Module12("test")))
print([cls.__name__ for cls in Module12.mro()])

# output:
# module-1:test
# ['Module12', 'BaseModule1', 'BaseModule2', 'BaseModule', 'object']
