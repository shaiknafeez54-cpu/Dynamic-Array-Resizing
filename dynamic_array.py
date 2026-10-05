class DynamicArray:
    def __init__(self):
        self.a = [None] * 2
        self.size = 0
        self.allocations = 1
        self.copies = 0

    def add(self, x):
        if self.size == len(self.a):
            new = [None] * (len(self.a) * 2)
            self.allocations += 1

            for i in range(self.size):
                new[i] = self.a[i]
                self.copies += 1

            self.a = new

        self.a[self.size] = x
        self.size += 1


d = DynamicArray()

for i in range(10):
    d.add(i)

print("Array:", d.a[:d.size])
print("Allocations:", d.allocations)
print("Copies:", d.copies)
print("Normal add: O(1)")
print("Add during resize: O(n)")
print("Amortized add: O(1)")
