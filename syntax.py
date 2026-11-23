# n = 3 #int  
# price = 9.99 #float
# name = 'jay' #string
# list_items = [1,2,3] #list
# tuple_items = (1,2,3) #tuple
# set_items = {1,2,3} #set
# dict_items = {"a":1,"b":2,"c":3} #dictoinary(key value pair)
# print(36/5) # use print to whenever you need to show results
# print(2**6) # exponent operator
# print(1 + 3 * 2) # ans = 7 #order of execution -  Division-Multiplication-Addition-Subtraction
# print((1+3)*2) # ans = 8 #enforce precedence with parentheses
# # Boolean values - True, False #first letter capital
# # negate with "not" - not True, not False 
# # Boolean Operators - and, or #case sensitive, always small

# #True and False are 1 and 0 but with different keywords
# print(True and False) #gives False as 1 and 0 is 0
# print(True or False) # gives True ass 1 or 0 is 1
 
# # Comparision Operator -> ==,>,<,!=

# # None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# # All other values are True
# bool(0)      # => False
# bool("")     # => False
# bool([])     # => False
# bool({})     # => False
# bool(())     # => False
# bool(set())  # => False
# # bool(4)      # => True
# # bool(-6)     # => True

# #using boolean operators (and, or) on integers 
# #will assume integers as boolean value, but returns the real integers
# # Thats called casting
# # Don't get confused between boolean operators (and,or) and bitwise operator(&,|) 
# bool(0) # bool(0) = False
# bool(2) # bool(2) = True 
# print(0 or 2) # true i.e will print the integer
# print(0 and 2) # false i.e will print 0

# # is vs ==
# # is checks if the if two variable refer for same objects
# # == check if both the variable has the same value

# a = [1,2,3,4]  #a is defined
# b = a # assigned b to a
# print(b is a) # true because a and b are assigned the same object
# print(b == a) # true because b and a has same values
# # but now lets define b
# b = [1,2,3,4] 
# print(b is a) # false because b and a are now assigned different objects i.e b and a are now bointing towards different objects
# print(b == a) # is still true because both objects has equal values

# "hello world" #string
# # a string can be treated as list of characters
# print("hello"[1]) # ->e also indexing in string starts from 0
# print(len("i love python")) # space is also counted as character

# #formated string
# name = "Rieko"
# print(f"my name is {name}")
# print(f"{name} has {len(name)} letters")

# # About the None object 
# # ->use is None and is not None when comparing with None
# # ->use == for everything else.


# print("Hello")                 # Hello  (then moves to a new line)

# print("Hello", end="!") # this will not print the next code in next line, It will print in the same line as we have replaced the next line using end keyword
# print("a","b","c") # by default separated by space
# # we can replace the space with something else using sep key word
# print("a","b","c", sep="-")

# # to take string input, use input keyword
# # name = input("type your name here: ")
# # age = int(input("Type your age here: "))

# # Normal If else (4 Line)
# age = 20
# if age >=18:
#     status = "adult"
# else:
#     status = "minor"
    
# # Ternary operator (3 parts 1 line)
# status = "adult" if age >= 18 else "minor"
# print(status)

# # Slicing
# lis = [1,3,5,6,4,2]
# print(lis[1:4]) # starts from index no. 1 till index 4 but last index item is not included in result
# print(lis[2:]) # starts from index 2 till end
# print(lis[:4]) # from start till index 4 but item at last index is not included
# print(lis[::3]) # from index 0 to end but every 3rd item
# # reversing the list using slicing
# print(lis[::-1]) # the whole list but from end 

# # combining the list
# l1 = [1,2,3]
# l2 = [4,5,6] # new list = [1,2,3,4,5,6], original will stay unchanged
# print(l1+l2)
# lis.extend([7,8]) # extends the list, orignaal changes
# print(lis)
# # checking in the list
# print(9 in lis)
# # Copying 
# a = [1,2]
# b = a 
# print(a is b)# here a is not a copy of b rather a and b both points towards the same list
# # to make a copy of list using a copy keyword
# b = a.copy()
# print(b)
# # or  
# b = a[:]
# print(b)
# print(a is b)

# # Case/Match statement
# command = "run"

# match command:
#     case "run":
#         print("robot started running")
#     case "speak" | "say_hi": # multiple command using OR operator
#         print("the robot said hi")
#     case code if command.isdigit(): # Conditions
#         print("Robot executed a code :{code}")
#     case _: # _ is like default/else
#         print("Invalid command")
        

# # For Loop over a list of string
# for animal in ["cat", "dog", "mouse", "donkey"]:
#     print(f"{animal} is a Mammal")
    

# # While loop 
# # -- execute until the conddition is no longer met
# x=1
# while x<=5:
#     print (x)
#     x=x+1
    
# # Exception Handling with example
# stock = 10
# price = 2.0

# # enter_quant = input("Enter Quantity : ")
# enter_quant = 20
# try:
#     quantity = int(enter_quant)
#     if quantity > stock:
#         raise ValueError(f'only {stock} left in stock') # Custom error based on the variable stock
#     total = quantity*price
# except ValueError as e:
#     print("please enter a number")
# else:
#     print(f"Order placed. Total is {total}")
# finally:
#     print("session closed") # Finnaly always runs
    

# # with open - replaces traditional try and finally

# # old way
# f = open("myfile.txt")
# try:
#     data = f.read()
# finally:
#     f.close()
    
# # new way 
# with open("myfile.txt") as f:
#     data = f.read()
    
# # read a file line by line
# with open("myfile.text") as f:
#     for line in f:
#         print(line)
        
# # writing a dictonary as a plain text 
# contents = {"aa": 12, "bb": 21}
# with open("file1.txt", "w") as file: # write operation
#     file.write(str(contents)) # file.write can only write string
#     # so we use str to convert content into string/text
    
# # writing a dictionary as JSON (iterable)
# import json
# contents = {"a":12, "b":13}
# with open("file2.txt", "w") as file2:
#     file.write(json.dumps(contents))
    
# # reading from a file
# with open("file.txt") as f:
#     contents = f.read() # read a string from file
# print(contents) 
    
# with open("file.txt", "r") as f:
#     contents = json.load(f)
# print(contents) # it is a real dictionary again

# # Funtions in python
# # Returning Multiple values 
# def swap(x,y):
#     return y,x

# x, y = 1, 2
# x, y = swap(x,y)
# print(x,y)

# # Define local variable in the function and Global variable outside it. using global variable to define a local needs global keyword
# count = 100 # global variable
# # global keyword inside the funtion indicates that particular var lives in the global scope
# def test():
#     count = 25 # local variable
#     print("count inside the funtion", count)
# test()
# print("count outside the funtion", count)


# nested funtion
# def create_adder(x):
#     def adder(y):
#         return x + y # adder funtion returns add of x+y
#     return adder # create_adder returns the nested adder funtion

# add_number_10 = create_adder(10)
# print(add_number_10(4))

# Lambda Funtion
# print((lambda x: x > 2)(3))
# print((lambda x,y : x**2 + y**1)(2,1))

# built in funtions
# def add_10(x):
#     return x+10

# # 1. Map() - does the same thing to every item. 
#     # gives back a lazy “map object”, so wrap it in list() to see the results.
# print(list(map(add_10, [1,3,5])))
# print(list(map(lambda x: x*3, [1,2,3]))) # map with lambda
# print(list(map(max, [4,3,5], [7,1,3]))) # map with max funtion to compare 2 list

# # 2. Filter() - keep only the items to pass a test
# print(list(filter(lambda x: x>5, [1,2,3,4,5,6,7,8])))


# # CLASS in Python
# class Product:
#     store = "ShopFlow"
#     def __init__(self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock
        
#     def describe(self):
#         return f"{self.name} : ${self.price} ({self.stock} left)"
    
#     def is_in_stock(self):
#         return self.stock>0
    
# mug = Product("Mug", 10, 30)
# shirt = Product("Shirt", 16.99, 6)

# print(mug.describe())
# print(shirt.is_in_stock())
# print(mug.store)
# shirt.store = "ClothFlow"
# print(mug.store)
# print(shirt.store)

# INHERITENCE in Python

# class Product:
    
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
    
#     def describe(self):
#         return f"{self.name} : {self.price}"
    
#     def shipping(self):
#         return "ships in 3 to 5 days"
    
# class DigitalProduct(Product):
        
#         def __init__(self, name, price, url):
#              super().__init__(name, price)
#              self.url = url
# # The new word here is super(). It means “the parent class.” So super().__init__(name, price) means: “run the parent’s __init__ to set up the name and price for me.” The child then only adds what’s new, the download_url.

#         def shipping(self): # Method overriding
#             return "instant download"
        
# ebook = DigitalProduct("Python", 9, "www.url.com")
# print(ebook.describe())
# print(ebook.url)
# val = 3
# mug = Product("Mug", val)
# print(ebook.shipping())
# print(mug.shipping())
# val = 6
# print(val)
# print(mug.describe())
# print(isinstance(ebook, DigitalProduct))
# print(isinstance(ebook, Product))
# print(isinstance(mug, DigitalProduct))



class Book:
    def __init__(self, title, name):
        self.name = name
        self.title = title
    def describe(self):
        return f"{self.title} by {self.name}"
    
class Ebook(Book):
    def __init__(self, title, name, size):
        super().__init__(title, name)
        self.size = size 
            
book1 = Book("Atomic Habits", "James Clear")
book2 = Book("The Alchemist", "Paulo Coelho")
ebook1 = Ebook("The brain", "David Englman", 23)
print(book1.describe())
print(book2.describe())
print(ebook1.describe())

