#!/usr/bin/env python
# coding: utf-8

# In[19]:


# 1
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def delete_zero_sum_nodes(head):
    if not head:
        return head

    dummy = Node(0)
    dummy.next = head
    current = dummy

    running_sum = 0
    sum_dict = {}

    while current:
        running_sum += current.data
        if running_sum in sum_dict:
            prev = sum_dict[running_sum]
            prev.next = current.next
        else:
            sum_dict[running_sum] = current
        current = current.next

    return dummy.next

head = Node(3)
head.next = Node(2)
head.next.next = Node(-1)
head.next.next.next = Node(1)
head.next.next.next.next = Node(-2)
head.next.next.next.next.next = Node(4)

print("Original Linked List:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

head = delete_zero_sum_nodes(head)

print("Modified Linked List:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")


# In[20]:


#2
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse_in_groups(head, k):
    if not head or k <= 1:
        return head

    current = head
    prev = None
    count = 0

    while current and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1
    if current:
        head.next = reverse_in_groups(current, k)

    return prev


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

print("Original Linked List:")
print_linked_list(head)

k = 3  

head = reverse_in_groups(head, k)

print("Modified Linked List:")
print_linked_list(head)


# In[21]:


#3
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def merge_alternate(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    current1 = head1
    current2 = head2
    while current1 and current2:
        next1 = current1.next
        next2 = current2.next

        current2.next = next1
        current1.next = current2

        current1 = next1
        current2 = next2

    return head1


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)

head2 = Node(4)
head2.next = Node(5)
head2.next.next = Node(6)

print("First Linked List:")
print_linked_list(head1)

print("Second Linked List:")
print_linked_list(head2)

head1 = merge_alternate(head1, head2)

print("Merged Linked List:")
print_linked_list(head1)


# In[22]:


#4
def count_pairs_with_sum(arr, target_sum):
    count = 0
    num_dict = {}

    for num in arr:
        complement = target_sum - num

        if complement in num_dict:
            count += num_dict[complement]

        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    return count

arr = [1, 5, 7, -1, 5]
target_sum = 6

pair_count = count_pairs_with_sum(arr, target_sum)
print(f"Number of pairs with sum {target_sum}: {pair_count}")


# In[23]:


#5
def find_duplicates(arr):
    duplicates = []
    num_dict = {}

    for num in arr:
        if num in num_dict:
            duplicates.append(num)
        else:
            num_dict[num] = 1

    return duplicates

arr = [1, 2, 3, 2, 4, 5, 3, 6]
duplicate_nums = find_duplicates(arr)
print("Duplicate numbers:", duplicate_nums)


# In[24]:


#6
def find_kth_largest_smallest(arr, k):
    sorted_arr = sorted(arr)
    kth_largest = sorted_arr[-k]
    kth_smallest = sorted_arr[k-1]
    return kth_largest, kth_smallest

arr = [9, 4, 7, 1, 5, 2, 8, 3, 6]
k = 3

kth_largest, kth_smallest = find_kth_largest_smallest(arr, k)
print(f"Kth largest number: {kth_largest}")
print(f"Kth smallest number: {kth_smallest}")


# In[25]:


# 7
def move_negative_elements(arr):
    n = len(arr)
    neg_idx = 0

    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[neg_idx] = arr[neg_idx], arr[i]
            neg_idx += 1

    return arr

arr = [4, -3, 2, -5, -1, 0, -2, 6, -7]
result = move_negative_elements(arr)
print("Array with negative elements moved to one side:", result)


# In[26]:


# 8
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


def reverse_string(input_string):
    stack = Stack()
    reversed_string = ""

    for char in input_string:
        stack.push(char)
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)


# In[27]:


#9

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


def evaluate_postfix(expression):
    stack = Stack()

    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char not in operators:
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if operand1 is None or operand2 is None:
                raise ValueError("Invalid postfix expression")

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            stack.push(result)

    final_result = stack.pop()

    if stack.is_empty() and final_result is not None:
        return final_result
    else:
        raise ValueError("Invalid postfix expression")

postfix_exp = "523*+"
result = evaluate_postfix(postfix_exp)
print("Result:", result)

 


# In[28]:


#10

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                raise IndexError("Queue is empty")
                
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def is_empty(self):
        return not self.enqueue_stack and not self.dequeue_stack

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  
print(queue.dequeue())  

queue.enqueue(4)
queue.enqueue(5)

print(queue.dequeue())  
print(queue.dequeue())  
print(queue.dequeue())  

print(queue.is_empty()) 

