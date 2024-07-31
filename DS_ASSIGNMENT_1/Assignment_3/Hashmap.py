#seperate chaning implementation
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)

    def __str__(self):
        return str(self.key) + " : " + str(self.value)

class HashTableChaining:
    def __init__(self):
        self.size = 0
        self.capacity = 5
        self.data = [[] for _ in range(self.capacity)]

    def get_size(self):
        return self.size

    def find(self, key):
        index = hash(key) % self.capacity
        for entry in self.data[index]:
            if entry.key == key:
                return True
        return False

    def insert(self, key, value):
        entry = Entry(key, value)
        index = entry.hash % self.capacity

        print("Inserting key:", key, "at index:", index)
        for i in range(len(self.data[index])):
            if self.data[index][i].key == key:
                self.data[index][i] = entry
                return
        
        self.data[index].append(entry)
        self.size += 1

    def remove(self, key):
        index = hash(key) % self.capacity
        for i in range(len(self.data[index])):
            if self.data[index][i].key == key:
                del self.data[index][i]
                self.size -= 1
                return

    def get(self, key):
        index = hash(key) % self.capacity
        for entry in self.data[index]:
            if entry.key == key:
                return entry.value
        return None

    def print_table(self):
        for i in range(self.capacity):
            print("Bucket", i, ":")
            for entry in self.data[i]:
                print(entry, end=" -> ")
            print()
        print("-------------")

hash_table = HashTableChaining()
hash_table.insert("roll no 1", 123)
hash_table.insert("roll no 2", 112)
hash_table.print_table()
hash_table.remove("roll no 1")
hash_table.print_table()
hash_table.remove("roll no 7")
hash_table.print_table()

#----------------------------------------------
# Open Addressing Implementation (Linear Probing)
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)

    def __str__(self):
        return str(self.key) + " : " + str(self.value)

class HashTableOpenAddressing:
    def __init__(self, capacity=5):
        self.size = 0
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.deleted = object()  #  marker for deleted entries

    def get_size(self):
        return self.size

    def find(self, key):
        index = self.__find_index(key)
        return index is not None

    def __find_index(self, key):
        index = hash(key) % self.capacity
        original_index = index

        while self.data[index] is not None:
            if self.data[index] != self.deleted and self.data[index].key == key:
                return index
            index = (index + 1) % self.capacity
            if index == original_index:
                break
        return None

    def insert(self, key, value):
        if self.size >= self.capacity * 0.7:
            self.__resize()

        entry = Entry(key, value)
        index = hash(key) % self.capacity
        original_index = index

        while self.data[index] is not None and self.data[index] != self.deleted:
            if self.data[index].key == key:
                self.data[index] = entry
                return
            index = (index + 1) % self.capacity
            if index == original_index:
                break

        self.data[index] = entry
        self.size += 1

    def __resize(self):
        old_data = self.data
        self.capacity *= 2
        self.data = [None] * self.capacity
        self.size = 0

        for entry in old_data:
            if entry is not None and entry != self.deleted:
                self.insert(entry.key, entry.value)

    def remove(self, key):
        index = self.__find_index(key)
        if index is not None:
            self.data[index] = self.deleted
            self.size -= 1

    def get(self, key):
        index = self.__find_index(key)
        if index is not None:
            return self.data[index].value
        return None

    def print_table(self):
        for i in range(self.capacity):
            if self.data[i] is not None and self.data[i] != self.deleted:
                print("Index", i, ":", self.data[i])
            else:
                print("Index", i, ": None")
        print("-------------")

hash_table = HashTableOpenAddressing()
hash_table.insert("roll no 1", 123)
hash_table.insert("roll no 2", 112)
hash_table.print_table()
hash_table.remove("roll no 1")
hash_table.print_table()
hash_table.remove("roll no 7")
hash_table.print_table()
