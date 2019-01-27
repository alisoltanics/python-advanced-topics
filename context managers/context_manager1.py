"""Opens the file, writes to it and then closes
   the file even if exception occurs.
"""

with open('hello.txt', 'w') as file:
    file.write('hello, world!')
