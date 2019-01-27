from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        print("first runs this.")
        file = open(name, 'w')
        yield file
    finally:
        print("last runs this.")
        file.close()


with managed_file('hello.txt') as file:
     print("second runs this.")
     file.write('hello, world!')
     file.write('bye now')
