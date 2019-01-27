class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("first runs this")
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("last runs this")
        if self.file:
            self.file.close()


with ManagedFile('hello.txt') as f:
    print("second runs this")
    f.write('hello, world!')
    f.write('bye now')
