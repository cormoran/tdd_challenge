class Stack():
    def __init__(self):
        self.size_ = 0

    def is_empty(self):
        return self.size_ == 0

    def push(self, value):
        self.value = value
        self.size_ += 1

    def top(self):
        return self.value

    def size(self):
        return self.size_
