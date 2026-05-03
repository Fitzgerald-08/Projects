def int_convert(integer):
    """Properly convert a given input to an integer using exceptions"""
    try:
        number = int(integer)
    except ValueError:
        return None
    else:
        return number


# When you want to use a variable as an "accumulator", it has to be declared
# outside a while loop, otherwise, the variable value's will reset to 0 in every iteration
