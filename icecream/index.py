from icecream import ic

def double(x):
    return x * 2

def is_valid(valid:bool):
    if valid:
        ic()
    else:
        ic()


ic.configureOutput(includeContext=True)
is_valid( valid = True )
ic(double(4))
ic(double(7))
