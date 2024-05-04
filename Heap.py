class MinHeap:
    def __init__(self):
        self.heap = []

    def build(self, lst):
        self.heap = lst[:]
        for i in reversed(range(len(self.heap)//2)):
            self.heapify(i)

    def insert(self, val):
        self.heap.append(val)
        self.sift_up(len(self.heap) - 1)

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_val = self.heap.pop()
        self.heapify(0)
        return min_val

    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

def sift_up(self, i):
        parent = (i - 1) // 2
        if parent >= 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.sift_up(parent)
    
        

def print_tree(heap, index=0, indent=0):
    if index < len(heap):
        print_tree(heap, index * 2 + 2, indent + 4)  # Print right subtree
        print(' ' * indent, heap[index])            # Print current node 
        print_tree(heap, index * 2 + 1, indent + 4) 

if __name__ == "__main__":
    # Create a new MinHeap
    heap = MinHeap()

    # Insert elements
    heap.insert(3)
    heap.insert(2)
    heap.insert(1)

    # Print the heap as a tree
    print("Heap after insertions: ")
    print_tree(heap.heap)

    # Remove the minimum element
    min_val = heap.remove()
    print("Removed minimum value: ", min_val)

    # Print the heap as a tree after removal
    print("Heap after removal: ")
    print_tree(heap.heap)





class MaxHeap(MinHeap):
    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def sift_up(self, i):
        parent = (i - 1) // 2
        if parent >= 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.sift_up(parent)
        
    def build(self, arr):
        self.heap = arr
        for i in reversed(range(len(arr)//2)):
            self.heapify(i)

    def insert(self, val):
        self.heap.append(val)
        self.sift_up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) > 1:
            max_val, self.heap[0] = self.heap[0], self.heap[-1]
            self.heap.pop()
            self.heapify(0)
        elif len(self.heap) == 1:
            max_val = self.heap.pop()
        else:
            max_val = None
        return max_val