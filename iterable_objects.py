class NumbersContainerIterable: 
    def __init__(self, start_number, end_number):
        self.start_number = start_number
        self.end_number = end_number

    def __iter__(self):
        current_number = self.start_number
        while current_number < self.end_number:
            yield current_number
            current_number += 1

    def __next__(self):
        if self.start_number >= self.end_number:
            raise StopIteration
        current_number = self.start_number
        self.start_number += 1
        return current_number

for x in NumbersContainerIterable(1, 5):
    print(x)
