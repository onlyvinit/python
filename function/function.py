# function is reusable block of code that can be used in programs multiple times for specific task. Instead of writing same logic again and again. 
# function is defined using def keyword followed by function name and parentheses.
# function can take parameters and return values.

# syntax of function
# def function_name(parameters):
#     statements    
#     return value

# example of function
def add(a, b):
    return a + b

# calling the function
result = add(5, 3)
print(result)

# function with default parameters
def greet(name="Guest"):
    return f"Hello, {name}!"

# calling the functionwith default parameter
print(greet())
print(greet("John"))

# function with variable number of arguments - allows you to pass a variable number of arguments to a function. This is useful when you don't know how many arguments will be passed to the function. You can use *args to accept a variable number of positional arguments and **kwargs to accept a variable number of keyword arguments.

# syntax of variable number of arguments :
# def function_name(*args):
#     statements    
#     return value

# example of function with variable number of arguments
def sum_all(*args):
    return sum(args)

# calling the function with variable number of arguments
print(sum_all(1, 2, 3, 4, 5))
   

# function with keyword arguments - allows you to pass arguments to a function using the name of the parameter. This makes it easier to understand what each argument represents and allows you to pass arguments in any order. 

# syntax of keyword arguments :
# function_name(parameter1=value1, parameter2=value2, ...)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# calling the function with keyword arguments 
print_info(name="John", age=30, city="New York")

# function with lambda expression - is a small anonymous function that can take any number of arguments, but can only have one expression. Lambda functions are often used for short, simple functions that are not worth defining with a full function definition.

# syntax of lambda function :
# lambda arguments: expression

add = lambda x, y: x + y
print(add(5, 3))

# function with list comprehension - is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expression can be anything, meaning you can put in all kinds of objects in lists.

# syntax of list comprehension :
# [expression for item in list]

squares = [x**2 for x in range(1, 6)]
print(squares)

# function with dictionary comprehension - is a concise way to create dictionaries. It consists of braces containing an expression followed by a for clause, then zero or more for or if clauses. The expression can be anything, meaning you can put in all kinds of objects in dictionaries.

# syntax of dictionary comprehension :
# {key_expression: value_expression for item in list}

numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(squares_dict) 

# function with generator expression - is a concise way to create generators. It consists of parentheses containing an expression followed by a for clause, then zero or more for or if clauses. The expression can be anything, meaning you can put in all kinds of objects in generators.

# syntax of generator expression :
# (expression for item in list)

evens = (x for x in range(1, 6) if x % 2 == 0)
print(list(evens))

# function with recursive function - is a function that calls itself in order to solve a problem. Recursive functions are often used to solve problems that can be broken down into smaller, similar subproblems.

# syntax of recursive function :
# def function_name(parameter):
#     if condition:
#         return function_name(new_parameter)
#     else:
#         return value
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# function with higher-order function - is a function that takes one or more functions as arguments and/or returns a function as its result. Higher-order functions are often used to create more abstract and flexible code.

# syntax of higher-order function :
# def higher_order_function(function):
#     function()

def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x**2, 5))

# function with closure - is a function that retains access to its enclosing scope even after the outer function has finished executing. Closures are often used to create functions that have private variables or to create functions that can be used as callbacks.

# syntax of closure :
# def outer_function():
#     variable = 10
#     def inner_function():
#         return variable
#     return inner_function

def outer_function():
    variable = 10
    def inner_function():
        return variable
    return inner_function

closure = outer_function()
print(closure())

# function with decorator - is a function that takes another function as an argument and extends its behavior without modifying the original function. Decorators are often used to add functionality to existing functions or to create reusable code.

# syntax of decorator :
# def decorator(function):
#     def wrapper(*args, **kwargs):
#         # do something before the function is called
#         result = function(*args, **kwargs)
#         # do something after the function is called
#         return result
#     return wrapper

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper

@decorator
def my_function():
    print("Inside the function.")

my_function()
