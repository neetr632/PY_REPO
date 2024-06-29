def function_in_A():
    from mod_b import (
        function_in_B,
    )  # LAZY LOADING CALLING THE MODULE FROM INSIDE THE FUNCTION

    function_in_B()
    print("function in A")


if (
    __name__ == "__main__"
):  # __name__method will help us to control the execution of the code, works like a lever that decides if the code below should run or not depending upon the way of execution
    function_in_A()

print(
    """
local symbol table:

1: Each function call creates its own local symbol table.
2: It stores information about local variables, parameters, and any variables defined within the function.
3: Exists only during the execution of that function call and is discarded when the function returns or raises an exception. 

Global Symbol Table:

1:It stores information about all global variables and functions defined in the current module.
2:Created when the module is imported or when the script is executed.
3:Remains in memory until the interpreter quits or the module is explicitly deleted.

"""
)
