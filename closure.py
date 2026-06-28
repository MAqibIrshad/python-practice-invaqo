

def multiplier(n:int): #a multiplier takes a number
    def multiply(x:int): #multiply is nested function (value to multiply by n)
        return x * n
    return multiply


#multiplier finishes and would normally lose its local variable n. However, because multiply uses n, Python keeps n alive inside the returned function.

mul = multiplier(5)

print(mul(2))