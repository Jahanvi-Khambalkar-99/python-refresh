# One-liner #1: reverse a list using slicing
nums = [1,2,3,4,5]
print(nums[::-1])

# One-liner #2: sort a list of tuples by the second item, using key=lambda
students = [("Jay", 173), ("Mia", 294), ("Leo", 111)]
students.sort(key = lambda x : x[1])
print(students)

# One-liner #3: a dict comprehension that maps each word to its length
words = ["mug", "shirt", "hat"]
dict_words = {i : len(i) for i in words}
print(dict_words)

# One-liner #4: count the letters in "banana" with Counter
from collections import Counter
print(Counter('banana'))

# One-liner #5: group words by their first letter with defaultdict(list)
from collections import defaultdict
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
groups = defaultdict(list)  # make the empty "groups" by default
for item in words:
    groups[item[0]].append(item) # "Find the list for this word's first letter, and add the word to it."
print(dict(groups))

# One-liner #6: append and pop from both ends of a deque
from collections import deque
d = deque([2, 3, 4])
d.pop()
d.popleft()
d.appendleft(1)
d.append(5)
print(d)

# One-liner #7: push 5 numbers onto a heap with heapq and pop the smallest
import heapq

h = []
heapq.heappush(h,5)
heapq.heappush(h,1)
heapq.heappush(h,8)
heapq.heappush(h,3)
heapq.heappush(h,2)
print(h)
smallest = heapq.heappop(h)
print(smallest)

# One-liner #8 : loop with enumerate and with zip
fruits = ["apple", "banana", "cherry"]
for item, price in enumerate(fruits):
    print(f"{item} : {price}")
names = ["Mug", "Shirt", "Hat"]
prices = [12, 20, 15]
for item in zip(names, prices):
    print(item) # output is one tuple pair
for n, p in zip(names, prices): # unpack the tuple
    print(n, p) 
