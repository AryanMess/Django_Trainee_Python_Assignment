class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
        yield


# Example usage
rectangle = Rectangle(10, 5)
for dimension in rectangle:
    print(dimension)
