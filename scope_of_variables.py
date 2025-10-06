#!/usr/bin/env python3
# Created By: Abdul
# Date: 10/5/2025
# scope of variables

# Global variable
variable_X = 10


def local_variable():
    variable_Y = 5
    print("Inside local_variable() -> variable_Y:", variable_Y)
    print("Accessing global variable_X from inside function:", variable_X)


def global_variable():
    global variable_Z
    variable_Z = 15
    print("Inside global_variable() -> variable_Z:", variable_Z)


# Function calls
if __name__ == "__main__":
    local_variable()
    global_variable()

print("Outside functions -> variable_X:", variable_X)
print("Outside functions -> variable_Z:", variable_Z)
