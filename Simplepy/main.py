def plus(num):
    return num + 1

def minus(num):
    return num - 1

def equal(var1,var2):
    if var1 == var2:
        return True

def greater(var1,var2):
    if var1 > var2:
        return True
    
def lower(var1,var2):
    if var1 < var2:
        return True
    
def greaterequal(var1,var2):
    if var1 >= var2:
        return True
    
def lowerequal(var1,var2):
    if var1 <= var2:
        return True
    
def average(list:list):
    return sum(list) / len(list)