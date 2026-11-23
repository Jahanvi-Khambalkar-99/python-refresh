# Single assignment
n = 3
n = "abc"

#multiple assignment
n,m,z = 2,"abc", True

# None is null(absence of value)
n= 3
n = None
print("n = ", n)

# if statements -> parenthesis are needed for multi-line conditions
n, m = 1, 2
if ((n>2 and n!=m) or n==m):
    n +=1
print(n)

#while loop
print("while loop")
n = 0 # we have to define the start
while n<5: 
    print(n) # n will be prin nted till n is less than 5
    n = n+1 # and we have to put increment to move forward in while loop. 
# it is not auto incremental like for loop

# for loop
print("for loop")
# looping from i=1 to i=4
for i in range(5): # indexing start from 0 and goes till 5 values
    print(i)
    
# arrays (called list in python)
arr = [1,2,3]

# can be used as stack 
arr.append(4) # use append to add in stack
arr.append(5)
print(arr)
arr.pop(0) # use pop to remove from stack, pop(index)
# so this will remove the number at 0th index which is 1
print(arr) 

# we can also insert value at any index 
# Note : this operation has O(n) time complexity
arr.insert(0,1) # will insert 1 at 0th index
arr.insert(1,7) # will insert 7 at 1th index
print(arr)

# constant time operation 
# we can read and reassign values to the aarray
arr[3]=10 
arr[5]=20
print(arr)

# initializing an array of size n with default value of 1 
n = 5
arr = [1]*n
print(arr)
print(len(arr))

arr = [1,2,3] 
print(arr[-1])
# thiss will print value at last index of array


# Important
# Slicing/sublist
arr = [1,2,3,4]
print(arr[1:3]) # indexing starts from 0
# so this will print item at index 1, 2 because the last index is non inclusive
print(arr[0:4])


# Unpacking 
a, b, c = [1,2,3] # no of items on both side needs to match 
print(a,b,c)

# Loop through the arrays
nums = [1,2,3,4,5]

# using index
for i in range(len(nums)):
    print(nums[i])
    
# without index
for n in nums:
    print(n)
    
# Use enumerate when you need both the index and value
# with index and value
for i,n in enumerate(nums):
    print(n,i)
    
# Loop through multiple arrays simultaniously
# with unpacking

# ----ZIP----
num1 = [1,3,5]
num2 = [2,4,6]
for n1, n2 in zip(num1, num2):
    print(n1, n2) 
    
# ----REVERSE AN ARRAY----
arr = [1,2,3,4,5]
arr.reverse()
print(arr)

# ----SORTING ----
arr = [5,4,7,3,8]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

# sorting array of strings
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

# sorting by length, 
# Uning a custom funtion
# ---- LAMBDA ----
arr.sort(key = lambda x : len(x))
print(arr)

# ----LIST COMPREHENSION----
arr = [i for i in range(0,5)]
print(arr)

# ---- 2D ARRAY ----
arr = [[0]*4 for i in range(4)]
print(arr)
arr = [[i for i in range(4)] for i in range(4)]
print(arr)


# Strings 
s="abc"
print(s[0:2]) # slicing the string

# Strings are immutable, we can not modify a string 

# we can add or update a string
s +="def"
print(s)

# a valid numeric string can be converted to number 
print(int("123") + int("123"))

# and number can be conveerted to string
print(str(123) + str(123))

# ----DELIMITER----
# Joining string from a list of string
string = ["ab","cd","ef"]
print("-".join(string)) # joining string using -

# Queue in pythone is double ended queue by default
from collections import deque
# initiating a queue
queue = deque()
# we can add and remove from both left and right side of queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

queue.popleft()
print(queue)
queue.appendleft(5)
print(queue)
queue.pop()
print(queue)
queue.append(6)
print(queue)


# Hash Set
#set has no duplicate values
my_set =set() # initiating a set
my_set.add(1) # adding elements to set 
my_set.add(2) # adding elements to set 
my_set.add(3) # adding elements to set 
print(my_set)
print(len(my_set))
# searching in a set
print(1 in my_set)
print(10 in my_set)
my_set.remove(2)
print(2 in my_set)
print(my_set)

# list to set
print(set([1,5,7]))

# ---SET COMPREHENTION----
my_set = {i for i in range(10)}
print(my_set)


# Hash Map
myMap={}
myMap['alice'] = 88 # to insert the value
myMap['bob'] = 66 
print(myMap)

#to modify the value
myMap["alice"] = 39
print(myMap)


# to search if a key exist in a hash map
print('alice' in myMap) #true
# to remove key from hashmap
myMap.pop('alice')
print('alice' in myMap)

# ----Dict Comprehension ---
#myMap = {key:value for key in range(5) } 
myMap = {i:i*3 for i in range(5)}
print(myMap)

# Looping through map

myMap = {'alice': 39, 'bob': 66}

#using key
for key in myMap:
    print(key,myMap[key])
    
# for value, using .values()
for val in myMap.values():
    print(val)
    
# to get both key and value, using .items
for key, val in myMap.items():
    print(key, val)
    
# --- Tuple ---
# Tuples are like arrays but immutable

tup = (1,2,3)
print(tup)
print(tup[0])
print(tup[-1]) 

# tuple is mainly used as key for hashmap, thats why the can't be modified(immutable)
myMap = {(1,2):3} # Tuple as key is hashable

# we can do tuples with hashsets as well
mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

# Heap - under the hood of array
import heapq
minHeap = [] # By defalt heap in python are min heap
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 8)

# in heap minimum value will always be at index 0
print(minHeap[0])


# No max heap by default
# workaround is to use min hip and then 
# multiply by -1 to push and pop

maxHip = []
heapq.heappush(maxHip, -3)
heapq.heappush(maxHip, -2)
heapq.heappush(maxHip, -1)

# amx is always at index 0
print(-1 * maxHip[0])
print("MaxHeap items: ")
while len(maxHip):
    
    print(-1 * heapq.heappop(maxHip))
    
# Build Heap from initial Set of Values
array = [2,5,3,6,9,8,4]
heapq.heapify(array)
print(array)
# A heap is not fully sorted. Only the smallest item is guaranteed to be first (nums[0]). 
# The rest just follow the parent ≤ children rule.




print("==============================================================================")
print("Syntax Test")

print("")
print("Reverse a list using slicing")
l1 = [1,2,3,4,5]
rev_l1 = l1[::-1]
print(rev_l1)

print("")
print("Sort a list of tuples by their second item, using key=lambda")
student = [("Jay", 173), ("Jay3", 294), ("Jay2", 111)]
student.sort(key=lambda x: x[1]) # using sort()
print(student)
# or using sorted()
sorted_student = sorted(student, key = lambda x : x[1])
print(sorted_student)


print("")
print("Sort a list of tuples by their second item, using key=lambda")
student = [("Jay", 173), ("Jay3", 294), ("Jay2", 111)]
student.sort(key=lambda x: x[1]) # using sort()
print(student)
# or using sorted()
sorted_student = sorted(student, key = lambda x : x[1])
print(sorted_student)