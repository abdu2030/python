class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def josephus(self, k):
        if self.head is None:
            return None

        current = self.head
        prev = None

        while current.next != current:
            for _ in range(k - 1):
                prev = current
                current = current.next

            #print("Removed:", current.data)

            prev.next = current.next

            if current == self.head:
                self.head = current.next

            current = current.next

        self.head = current
        return current.data
cll = CircularLinkedList()

n = int(input("Enter number of people: "))
k = int(input("Enter step: "))

for i in range(1, n + 1):
    cll.insert_end(i)

winner = cll.josephus(k)

print("Safe position is:", winner)


# def safe_position(n, k):
#     safe = 0

#     for i in range(1, n + 1):
#         safe = (safe + k) % i

#     return safe + 1


# n = int(input("Enter number of people: "))
# k = int(input("Enter step number: "))

# print("You should stand at position:", safe_position(n, k))