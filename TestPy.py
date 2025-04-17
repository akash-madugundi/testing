import ast

# High Complexity Functions (process)
def process(data):
    result = []
    for i in range(len(data)):
        if data[i] > 100:
            result.append(data[i] * 2)
        elif data[i] < 50:
            result.append(data[i] / 2)
        else:
            result.append(data[i] + 10)
    return result

# Low Maintainability Index (complex functions)
def calculate(a, b, c, d, e):
    if a > b:
        result = a * b * c * d * e
    else:
        result = (a + b) * (c + d) + e
    return result

# Large Files (This is just a simulation, actual file size is not managed here)
def simulate_large_file():
    return "a" * 600

# Deeply Nested Functions
def giant_method(data):
    for i in range(len(data)):
        if i % 2 == 0:
            if data[i] > 50:
                if data[i] % 5 == 0:
                    for j in range(100):
                        if j < 50:
                            print(f"Processing {data[i]} at {j}")
                        else:
                            print(f"Skipping {data[i]} at {j}")
                else:
                    print(f"Skipping {data[i]}")
            else:
                print(f"Processing {data[i]}")
        else:
            print(f"Skipping {data[i]}")

# Large Functions (too many lines, more than 50)
def large_function():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example data
    result = []
    for i in data:
        if i % 2 == 0:
            result.append(i * 2)
        else:
            result.append(i + 3)
    return result

# Feature Envy (Accessing fields of another object too frequently)
class MyClass:
    def __init__(self, name, email, address, phone, age, gender):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.age = age
        self.gender = gender

    def print_user_info(self):
        print(f"User Info: {self.name}, {self.email}, {self.age}, {self.gender}")

# Data Clumps (same group of variables used together in multiple places)
def update_user_info(name, email, address, phone, age, gender):
    print(f"Updated Info: {name}, {email}, {address}, {phone}, {age}, {gender}")

# Dead Code (Unused Variables)
def dead_code_example():
    unused_var = 100
    print("Some important logic here...")  # Unused variable not utilized

# Shotgun Surgery (Function with multiple changes happening together)
def shotgun_surgery():
    data = [1, 2, 3, 4, 5]
    for num in data:
        result = num * 2
        if result > 5:
            print(f"Result is greater than 5: {result}")
        else:
            print(f"Result is less than or equal to 5: {result}")
        print(f"Processed number: {num}")

# Long Lambdas (Lambdas with too many elements)
long_lambda = lambda x, y, z, a, b: x * y + z - a / b

# Useless Exceptions (Try block with empty exception handler)
def useless_exception():
    try:
        x = 10 / 0
    except ZeroDivisionError:
        pass

# Duplicate Code (Repeated blocks)
def do_something():
    x = 10
    y = 20
    return x + y

def do_something_else():
    x = 10
    y = 20
    return x + y

# Large Classes (Class with more than 10 methods)
class LargeClass:
    def method1(self): pass
    def method2(self): pass
    def method3(self): pass
    def method4(self): pass
    def method5(self): pass
    def method6(self): pass
    def method7(self): pass
    def method8(self): pass
    def method9(self): pass
    def method10(self): pass

# Too Many Returns (Multiple return points in function)
def too_many_returns(x):
    if x < 5:
        return "Less than 5"
    elif x > 10:
        return "Greater than 10"
    else:
        return "Between 5 and 10"

# Global Variables
global_var = 100
def update_global():
    global global_var
    global_var += 10

# Large Parameters (Function with more than 5 parameters)
def large_parameters(name, email, address, phone, age, gender, city, state):
    print(f"Name: {name}, Email: {email}, Address: {address}, Phone: {phone}, Age: {age}, Gender: {gender}, City: {city}, State: {state}")

if __name__ == "__main__":
    # Sample call to some functions
    process([10, 20, 30])
    calculate(10, 20, 30, 40, 50)
    simulate_large_file()
    giant_method([1, 2, 3, 4, 5])
    large_function()
    update_user_info("John", "john@example.com", "123 Street", "555-1234", 30, "M")
    dead_code_example()
    shotgun_surgery()
    useless_exception()
    do_something()
    do_something_else()
    large_class = LargeClass()
    large_class.method1()
    large_parameters("John", "john@example.com", "123 Street", "555-1234", 30, "M", "New York", "NY")
    update_global()
