def my_method(arg1, arg2):
    return arg1 + arg2

print my_method(5, 6)


def my_long_method(arg1, arg2, arg3, arg4):
    return arg1 + arg2 + arg3 + arg4

print my_long_method(1, 2, 3, 4)

def addition_simplified(*args):
    return sum(args)

print addition_simplified(1, 2, 3, 4, 5, 6)


# Args is a tuple of arguments and kwargs is a dictionary of arguments
# as shown in the example below
def what_are_kwargs(*args, **kwargs):
    print args
    print kwargs


what_are_kwargs(12, 34, 56, name='Jose', loc='UK')

