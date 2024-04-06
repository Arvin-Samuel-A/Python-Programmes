Memory_Table = {}

def Fibonacci(Number : int):

    if (Number in Memory_Table):

        return Memory_Table[Number]
    
    if (Number <= 1):

        Value = Number

    else:

        Value = Fibonacci(Number - 1) + Fibonacci(Number - 2)

    Memory_Table[Number] = Value

    return Value