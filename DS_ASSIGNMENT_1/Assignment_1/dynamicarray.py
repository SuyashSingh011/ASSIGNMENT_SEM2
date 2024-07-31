class DynamicArray:
    def __init__(self):
        self.arr = []

    def insert(self, index, value):
        if index < 0 or index > len(self.arr):
            print("Invalid index")
            return
        self.arr.insert(index, value)

    def delete_at_index(self, index):
        if index < 0 or index >= len(self.arr):
            print("Invalid index")
            return
        del self.arr[index]

    def get_size(self):
        return len(self.arr)

    def isempty(self):
        return len(self.arr) == 0

    def rotate_right(self, k):
        if not self.arr or k <= 0:
            return
        k %= len(self.arr)
        self.arr = self.arr[-k:] + self.arr[:-k]

    def reverse(self):
        self.arr.reverse()

    def append(self, value):
        self.arr.append(value)

    def prepend(self, value):
        self.arr.insert(0, value)

    def merge(self, other):
        merged = DynamicArray()
        merged.arr = self.arr + other.arr
        return merged

    def interleave(self, other):
        interleaved = DynamicArray()
        i, j = 0, 0
        while i < len(self.arr) and j < len(other.arr):
            interleaved.append(self.arr[i])
            interleaved.append(other.arr[j])
            i += 1
            j += 1
        while i < len(self.arr):
            interleaved.append(self.arr[i])
            i += 1
        while j < len(other.arr):
            interleaved.append(other.arr[j])
            j += 1
        return interleaved

    def get_middle_element(self):
        if not self.arr:
            print("Dynamic array is empty")
            return -1
        return self.arr[len(self.arr) // 2]

    def index_of(self, value):
        if value in self.arr:
            return self.arr.index(value)
        return -1

    def split_at_index(self, index):
        if index < 0 or index > len(self.arr):
            print("Invalid index")
            return None
        second_array = DynamicArray()
        second_array.arr = self.arr[index:]
        self.arr = self.arr[:index]
        return second_array

    def resize(self, factor):
        if factor <= 0:
            print("Invalid factor")
            return
        self.arr = self.arr * factor

    def print_array(self):
        print(" ".join(map(str, self.arr)))

arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.print_array()

arr.insert(2, 5)
arr.print_array()

arr.delete_at_index(2)
arr.print_array()

print("Size:", arr.get_size())
print("Is empty?", "Yes" if arr.isempty() else "No")

arr.rotate_right(2)
arr.print_array()

arr.reverse()
arr.print_array()

arr.prepend(0)
arr.print_array()

arr2 = DynamicArray()
arr2.append(5)
arr2.append(6)
arr2.append(7)

merged = arr.merge(arr2)
merged.print_array()

interleaved = arr.interleave(arr2)
interleaved.print_array()

print("Middle element:", arr.get_middle_element())

print("Index of 3:", arr.index_of(3))

second_array = arr.split_at_index(2)
arr.print_array()
second_array.print_array()

arr.resize(3)
arr.print_array()
