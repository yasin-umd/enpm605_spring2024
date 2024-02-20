import sys

# ----------------
# Slide 19
# ----------------
# print()
# print("Welcome", "to ENPM", 605)
# print("Welcome", "to ENPM", 605)
# print("Welcome", "to ENPM", 809, "E", sep="***")

# ----------------
# Slide 20
# ----------------

# # standard assignment
# name = "Guido van Rossum"
# # chained assignments
# x = y = 10
# print(x, y)
# # multiple assignments
# name, age, role = "Guido van Rossum", 64, "BDFL Emeritus"
# print(name, age, role)

# ----------------
# Slide 21
# ----------------
# a = 10

# print(type(a))  # <class 'int'>
# print(type(100.5))  # <class 'float'>
# print(type(print))  # <class 'builtin_function_or_method'>

# ----------------
# Slide 22
# ----------------
# a = 10
# b = 10.5
# c = "hello"

# print(id(a))  # 139869549249040
# print(id(b))  # 139869548203760
# print(id(c))  # 139869548514160
# print(id(10))  # guess the output
# print(id(10.5))  # guess the output
# print(id("hello"))  # guess the output


# ----------------
# Slide 28
# ----------------
# x = "hello"
# print(type(x))  # <class 'str'>
# x = 10.5
# print(type(x))  # <class 'float'>

# ----------------
# Slide 32
# ----------------
# x = 1

# if x == 1:
#     print("x is 1")

# print("outside code block")

# ----------------
# Slide 33
# ----------------
# x = 1

# if x == 1:
#     print("x is 1")
# else:
#     print("x is not 1")

# print("outside code block")

# ----------------
# Slide 34
# ----------------
# x = 5

# if x == 1:
#     print("x is 1")
# elif x == 2:
#     print("x is 2")
# elif x == 3:
#     print("x is 3")
# else:
#     print("x is not 1, 2, or 3")

# ----------------
# Slide 36
# ----------------
# x = [2]

# if x:
#     print("x is True")
# else:
#     print("x is False")

# ----------------

# print(bool(0))  # False
# print(bool(1))  # True
# print(bool(-2))  # True
# print(bool(""))  # False
# print(bool(" "))  # True

# x = "hello"
# print(bool(x))  # True

# ----------------
# Slide 37
# ----------------
# a = 1
# b = 2
# print(a == b)  # False
# print(a != b)  # True
# print(a > b)  # False
# print(a < b)  # True
# print(a >= b)  # False
# print(a <= b)  # True

# ----------------
# Slide 38
# ----------------
# a = "hello"
# b = 1
# print(bool(b and a))
# print(a and b)  # False
# print(a or b)  # True
# print(not a)  # False
# print(not b)  # True
# print(not (a and b))  # True
# print(not (a or b))  # False


# ----------------
# Slide 39
# ----------------
# x = "hello"
# print("ll" in x)  # True
# print("he" in x)  # True
# print("O" in x)  # False

# ----------------
# Slide 40
# ----------------
# a = "hello"
# b = 2
# print(a is b)  # False
# print(a is not b)  # True

# ----------------
# Slide 41
# ----------------
# a = None
# if a is None:
#     print("a is None")

# print(type(None))  # <class 'NoneType'>

# ----------------
# Slide 42
# ----------------

# number = 123
# print(type(number))  # <class 'int'>
# number_str = str(number)
# print(type(number_str))  # <class 'str'>
# # print(type(int(number_str)))

# ----------------
# Slide 43
# ----------------
# print("This string\nhas\nbeen\nsplit")
# print("1\t2\t3\t4")
# print("He said: \"I'm here!\"")
# print('He said: "I\'m here!"')
# print('''He said: "I'm here!"''')
# print("""He said: "I'm here!" """) # note the space before the ending triple quotes
# print("C:\\Users\\tony\\notes.txt") # TODO: Fix this

# ----------------
# Slide 45
# ----------------
# name = "John"
# age = 30
# print("His name is %s and he is %d years old. %s" % (name, age, name))

# ----------------
# Slide 46
# ----------------
# name = None
# age = 25
# print("Her name is {} and she is {} years old.{}".format(name, age, name))
# # With positional arguments
# print("Her name is {1} and she is {0} years old. {1}".format(age, name))

# ----------------
# With keyword arguments
# print("Her name is {name} and she is {age} years old.".format(name="Alice", age=25))

# ----------------
# Slide 47
# ----------------

# print(f"Her name is {name} and she is {age} years old. {age} {location}")  # note the f before the string
# print(F"Her name is {name} and she is {age} years old.")  # note the F before the string

# ----------------
# Slide 48
# ----------------
# first_name = "John"
# last_name = "Doe"
# print(first_name + " " + last_name)  # John Doe
# ----------------
# words = ["Hello", "world"]
# sentence = " ".join(words)
# print(sentence)  # Hello world
# ----------------
# first_name = "John"
# last_name = "Doe"
# full_name = "%s %s" % (first_name, last_name)
# print(full_name)  # John Doe
# full_name = "{} {}".format(first_name, last_name)
# print(full_name)  # John Doe
# full_name = f"{first_name} {last_name}"
# print(full_name)  # John Doe

# ----------------
# Slide 49
# ----------------
# print(len("hello"))  # 5
# ----------------
# print(str(3), type(str(3)))  # 3 <class 'str'>
# print(str(3 + 4), type(str(3 + 4)))  # 7 <class 'str'>
# ----------------
# greeting = "hello"
# print(greeting.capitalize())  # Hello
# print(greeting)  # hello
# greeting = "Hello"
# print("hello".capitalize())  # Hello

# ----------------
# Slide 51
# ----------------
# print("hello"[0])  # h
# greeting = "hello"
# print(greeting[1])  # e
# ----------------
# print("hello"[-5])  # h
# greeting = "hello"
# print(greeting[-4])  # e
# # ----------------
# # print("hello"[5])
# greeting = "hello"
# greeting = "cello"
# greeting[0] = "c"
# print(greeting)

# ----------------
# Slide 53
# ----------------
# greeting = "hello"

# # # Slicing with positive indices
# print(greeting[0:3])  # from start up to index 2
# print(greeting[:3])  # from start up to index 2
# print(greeting[:5])  # from start up to index 4
# print(greeting[:])  # from start to end

# # # Slicing with negative indices
# print(greeting[-5:])  # from start to end
# greeting = "hello"
# print(greeting[-5:-2])  # from start up to index 2

# # # Slicing with positive and negative indices
# print(greeting[-5:2])  # from start up to index 1
# print(greeting[-5:4])  # from start up to index 3

# ----------------
# Slide 54
# ----------------
# quote = "Learn Python, be happy!"
# print(quote[-12:-18:-1])
# a = "h" * 4097
# b = "h" * 4097
# print(id(a), id(b))
# #----------------
# print(quote[::]) # Learn Python, be happy!
# print(quote[::1]) # Learn Python, be happy!
# # #----------------
# print(quote[::2])  # LanPto,b ap!
# print(quote[::3])  # LrPh,eay
# # #----------------
# print(quote[:8:-1])  # !yppah eb ,noh

# ----------------
# Slide 57
# ----------------
# a = "hello"
# b = "hello"
# c = "h" + "ello"
# d = "he" + "llo"
# d = "".join(["h", "e", "l", "l", "o"])
# e = "{0}{1}".format("h", "ello")

# print(a is b)  # True
# print(c is d)  # False
# print(a is d)  # False
# print(a is e)  # False

# ----------------
# Slide 58
# ----------------
# a = "hello"
# b = "hello"
# c = sys.intern("h" + "ello")
# d = sys.intern("he" + "llo")
# d = sys.intern("".join(["h", "e", "l", "l", "o"]))
# e = sys.intern("{0}{1}".format("h", "ello"))

# print(a is b)  # True
# print(c is d)  # True
# print(a is d)  # True
# print(a is e)  # True

print(3//2)  # 1
print(-3//2)

a, b = 200000000000000000000000000000, 200000000000000000000000000000
print(a is b)
