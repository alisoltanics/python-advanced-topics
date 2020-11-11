class Person:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr.startswith("ali"):
            return "you know me."
        raise AttributeError(
            "{} has no attribute {}".format(self.__class__.__name__, attr)
        )


person = Person("ali")
print(person.ali_asghar)
