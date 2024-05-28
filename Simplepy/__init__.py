def plus(var):
    return var + 1

def minus(var):
    return var - 1

def equal(var1,var2):
    if var1 == var2:
        return True
    
def not_equal(var1,var2):
    if not var1 == var2:
        return True
    
def greater(var1,var2):
    if var1 > var2:
        return True

def lower(var1,var2):
    if var1 < var2:
        return True

def itsin(value,list):
    if value in list:
        return True

def not_in(value,list):
    if value not in list:
        return True
