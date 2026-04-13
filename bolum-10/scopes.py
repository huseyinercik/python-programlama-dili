# Local scope
# Global scope

# x = "global scope"

# def my_func():
#     x = "local scope"
#     print(x)

# my_func()
# print(x)

# name = "Cinar"

# def changeName(newName):
#     global name
#     name = newName
#     print(name)

# changeName("Ada")
# print(name)

# name = "global string"

# def greeting():
#     name = "Cinar"

#     def hello():
#         name = "Ada"
#         print("hello ",name)

#     hello()
# greeting()

x = 50

def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)