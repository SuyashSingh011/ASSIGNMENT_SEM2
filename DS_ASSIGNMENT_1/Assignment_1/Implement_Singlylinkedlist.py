class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Insert an element at the specified index
    def insert(self, index, value):
        if index < 0 or index > self.size:
            print("Invalid index")
            return

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

        self.size += 1

    # Delete the element at the specified index
    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index")
            return

        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1

    # Return the size of the linked list
    def get_size(self):
        return self.size

    # Return true if the linked list is empty, false otherwise
    def is_empty(self):
        return self.size == 0

    # Rotate the linked list by k positions to the right
    def rotate_right(self, k):
        if k <= 0 or self.size == 0:
            return

        k = k % self.size
        curr = self.head
        for _ in range(self.size - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = self.head
        self.head = new_head

    # Reverse the linked list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # Append an element to the end of the linked list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        self.size += 1

    # Prepend an element to the beginning of the linked list
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # Merge two linked lists into a single linked list
    def merge(self, list1, list2):
        merged_list = LinkedList()
        curr1 = list1.head
        curr2 = list2.head

        while curr1 and curr2:
            if curr1.data < curr2.data:
                merged_list.append(curr1.data)
                curr1 = curr1.next
            else:
                merged_list.append(curr2.data)
                curr2 = curr2.next

        while curr1:
            merged_list.append(curr1.data)
            curr1 = curr1.next

        while curr2:
            merged_list.append(curr2.data)
            curr2 = curr2.next

        return merged_list

    # Interleave two linked lists into a single linked list   
    '''
    Interleaving two linked lists means creating a new linked list by alternately taking nodes from each of the two original linked lists.
For example, let's say we have two linked lists:
List 1: 1 -> 3 -> 5
List 2: 2 -> 4 -> 6
If we interleave these two lists, the resulting new linked list would be:
Interleaved List: 1 -> 2 -> 3 -> 4 -> 5 -> 6

    '''
    def interleave(self, list1, list2):
        interleaved_list = LinkedList()
        curr1 = list1.head
        curr2 = list2.head

        while curr1 and curr2:
            interleaved_list.append(curr1.data)
            interleaved_list.append(curr2.data)
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            interleaved_list.append(curr1.data)
            curr1 = curr1.next

        while curr2:
            interleaved_list.append(curr2.data)
            curr2 = curr2.next

        return interleaved_list

    # Return the middle element of the linked list
    def get_middle_element(self):
        if not self.head:
            print("Linked list is empty")
            return None

        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    # Return the index of the first occurrence of the specified element
    def index_of(self, value):
        curr = self.head
        index = 0
        while curr:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1

        return -1

    # Split the linked list into two linked lists at the specified index
    def split_at_index(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index")
            return None

        second_list = LinkedList()
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        second_list.head = curr.next
        curr.next = None
        self.size = index

        return second_list

    # Print the linked list
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

# Example usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.print_list()  # Output: 1 2 3 4

linked_list.insert(2, 5)
linked_list.print_list()  # Output: 1 2 5 3 4

linked_list.delete_at_index(2)
linked_list.print_list()  # Output: 1 2 3 4

print("Size:", linked_list.get_size())  # Output: Size: 4
print("Is empty?", linked_list.is_empty())  # Output: Is empty? False

linked_list.rotate_right(2)
linked_list.print_list()  # Output: 3 4 1 2

linked_list.reverse()
linked_list.print_list()  # Output: 2 1 4 3

linked_list.prepend(0)
linked_list.print_list()  # Output: 0 2 1 4 3

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

merged_list = linked_list.merge(list1, list2)
merged_list.print_list()  # Output: 1 2 3 4 5 6

interleaved_list = linked_list.interleave(list1, list2)
interleaved_list.print_list()  # Output: 1 2 3 4 5 6

print("Middle element:", linked_list.get_middle_element())  # Output: Middle element: 2

print("Index of 3:", linked_list.index_of(3))  # Output: Index of 3: 3

second_list = linked_list.split_at_index(2)
linked_list.print_list()  # Output: 0 2
second_list.print_list()  # Output: 1 4 3