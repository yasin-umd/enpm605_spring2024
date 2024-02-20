# ==================#
# --- List Type --- #
# ==================#

# # ----Slide 5 ---- #
# question = "What is blue and smells like red paint?"

# for character in question:
#     print(character)

# # ----Slide 6-1 ---- #
# fruits = ["apple", "banana"]
# result = fruits.append("orange")  # add orange to the list
# print(result)  # None
# print(fruits)  # ['apple', 'banana', 'orange']

# # ----Slide 6-2 ---- #
# fruit = "apple"
# upper_fruit = fruit.upper()  # Returns a new string, original is unchanged
# print(fruit)  # apple
# print(upper_fruit)  # APPLE

# # ----Slide 7 ---- #
# a = [1, 2, 3]
# b = [1, "hello", 3.5]
# c = ["a", [1, 2, 3.5], ["b", ["c", "d", 1, 2, 3]]]

# # ----Slide 8 ---- #
# fruits1 = ["apple", "banana", "cherry"]
# fruits2 = ["cherry", "banana", "apple"]
# fruits3 = ["apple", "banana", "cherry"]
# print(fruits1 == fruits2)  # False
# print(fruits1 is fruits2)  # False
# print(fruits1 == fruits3)  # True
# print(fruits1 is fruits3)  # False

# # ----Slide 9 ---- #
# x = [int, print, "cherry", 1, 2.5, print, str, str]
# print(x)


# # ----Slide 10 ---- #
# a = ["apple", "banana", 1]
# print(a)
# # ---
# a = list()  # []
# a = list("apple")  # ['a', 'p', 'p', 'l', 'e']
# a = list(["apple", "banana"])  # ['apple', 'banana']
# print(a)
# # ---
# # create an empty list
# square_num = []
# # use a loop to fill out the list
# for num in range(1, 5):
#     square_num.append(num * num)  # [1, 2, 9, 16]

# print(square_num)

# # ----Slide 11 ---- #
# s = "Have you got anything without spam?"
# vowel_list = [char for char in s if char in "aeiouy"]
# print(vowel_list)  # ['a', 'e', 'o', 'u', 'o', 'a', 'i', 'i', 'a', 'ou', 'a']

# # ----Slide 12 ---- #
# numbers = [3, 4, -5, 45, -55]
# numbers = [n if n > 0 else 0 for n in numbers]
# print(numbers)  # [3, 4, 0, 45, 0]

# # ----Slide 13 ---- #
# matrix = [
#     [0, 0, 0, 0],
#     [1, 1, 1, 1],
#     [2, 2, 2, 2],
#     [3, 3, 3, 3],
# ]

# # with list comprehension
# flattened = [num for row in matrix for num in row]
# print(flattened)  # [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

# # with a for loop
# flat = []
# for row in matrix:
#     for num in row:
#         flat.append(num)
# print(flat)  # [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

# # ----Slide 14 ---- #
# fruits = ["apple", "banana", "cherry", "pear", "kiwi"]
# print(fruits[1])  # banana
# print(fruits[-2])  # pear
# # A slice of fruits (Haha!)
# print(fruits[-4:-1])  # ['banana', 'cherry', 'pear']

# # ----Slide 15 ---- #
# fruits = ["apple", "banana", "cherry", "pear", "kiwi"]
# fruits[0] = "orange"  # ['orange', 'banana', 'cherry', 'pear', 'kiwi']

# fruits[1:3] = []  # ['orange', 'pear', 'kiwi']
# fruits[:] = ["orange", "orange", "orange"]  # ['orange', 'orange', 'orange']
# fruits[:] = ["apple"]  # ['apple']
# fruits[:] = "apple"  # ['a', 'p', 'p', 'l', 'e']

## ---- Exercise ---- #
# fruits = ["apple", "banana", "cherry", "pear", "kiwi"]
# # write code here
# print(fruits)  # ['apple', 'banana', 'cherry', [], 'kiwi']

# # ----Slide 16 ---- #
# fruits = ["apple", "banana", "cherry", "kiwi", "apple"]
# del fruits[0]
# print(fruits)  # ['banana', 'cherry', 'kiwi', 'apple']
# del fruits[1:]
# print(fruits)  # ['banana']
# del fruits
# print(fruits)  # NameError: name 'fruits' is not defined

# # ----Slide 17-1 ---- #
# fruits = ["apple", "banana"]
# fruits = ["kiwi"] + fruits  # ['kiwi', 'apple', 'banana']
# fruits = fruits + ["cherry"]  # ['kiwi', 'apple', 'banana', 'cherry']

# # ----Slide 17-2 ---- #
# fruits = ["apple"]
# fruits += ["banana"]  # ['apple', 'banana']
# fruits += "kiwi"  # ['apple', 'banana', 'k', 'i', 'w', 'i']

# # ----Slide 18 ---- #
# fruits = ["apple"]
# fruits.append("kiwi")  # ['apple', 'kiwi']

# fruits = ["apple"]
# fruits.extend(["kiwi"])  # ['apple', 'kiwi']

# fruits = ["apple"]
# fruits.insert(0, "kiwi")  # ['kiwi', 'apple']

# fruits = ["apple", "kiwi", "apple"]
# fruits.remove("apple")  # ['kiwi', 'apple']

# fruits = ["apple", "kiwi"]
# print(fruits.pop(1))  # kiwi

# fruits = ["apple", "kiwi"]
# fruits.clear()  # []

# # ----Slide 19 ---- #
#letters = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g"]
#print(letters[1][1][1])


# # ----Slide 20 ---- #
# fruits1 = ["apple"]
# fruits2 = fruits1
# print(fruits1 is fruits2)  # True
# ---
# fruits1 = ["apple"]
# fruits2 = fruits1
# fruits1.append("kiwi")
# fruits2.append("orange")
# print(fruits1)  # ['apple', 'kiwi', 'orange']
# print(fruits2)  # ['apple', 'kiwi', 'orange']

# # ----Slide 20 ---- SHALLOW COPY ---- #
# from copy import copy

# num1 = [1, [2]]
# num2 = copy(num1)  # SHALLOW COPY
# print(f"{num1=}", f"{num2=}")  # num1=[1, [2]] num2=[1, [2]]
# print(num1 is num2)  # False

# num1.append(3)
# print(f"{num1=}", f"{num2=}")  # num1=[1, [2], 3] num2=[1, [2]]

# num1[0] = 4
# print(f"{num1=}", f"{num2=}")  # num1=[4, [2], 3] num2=[1, [2]]

# num1[1].append(100)
# print(f"{num1=}", f"{num2=}")  # num1=[4, [2, 100], 3] num2=[1, [2, 100]]

# # ----Slide 22 ---- DEEP COPY ---- #
# from copy import deepcopy

# num1 = [1, [2]]
# num2 = deepcopy(num1)  # DEEP COPY
# print(f"{num1=}", f"{num2=}")  # num1=[1, [2]] num2=[1, [2]]
# print(num1 is num2)  # False

# num1.append(3)
# print(f"{num1=}", f"{num2=}")  # num1=[1, [2], 3] num2=[1, [2]]

# num1[0] = 4
# print(f"{num1=}", f"{num2=}")  # num1=[4, [2], 3] num2=[1, [2]]

# num1[1].append(100)
# print(f"{num1=}", f"{num2=}")  # num1=[4, [2, 100], 3] num2=[1, [2]]


# # ----Slide 23 ---- #
# num = [1, 2, 3, 1, 1]
# print(num.count(1))  # 3
# print('-' * 10)

# num = [2, 3, 2, 1, 3]
# print(num.index(3))  # 1
# print("-" * 10)

# num = [2, 3, 2, 1, 3]
# num.reverse()
# print(num)  # [3, 1, 2, 3, 2]
# print("-" * 10)

# num = ["a", "d", "ccc", "bb"]
# num.sort()
# print(num)  # ['a', 'bb', 'ccc', 'd']
# print("-" * 10)

# num = ["a", "d", "ccc", "bb"]
# new_num = sorted(num)
# print(num)  # ['a', 'd', 'ccc', 'bb']
# print(new_num)  # ['a', 'bb', 'ccc', 'd']


# # ----Slide 24 - Quiz ---- #
# a = [0, 1, [2, 3]]
# print(a.pop().pop())
# print("-" * 10)

# a = ["1", "2", "3"]
# print(a[1:])
# print("-" * 10)

# x = ["a", "b"]
# y = "cde"
# print(x.extend(y))
# print("-" * 10)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# output = [x for x in fruits if "a" in x]
# print(output)
# print("-" * 10)

# Use slicing to remove "apple", "banana", "cherry" from the list
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


