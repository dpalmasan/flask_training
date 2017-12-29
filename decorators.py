import functools

# Static methods are called decorators (are functions that are called before another functions)
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print "In the decorator!"
        func()
        print "After decorator"
    return function_that_runs_func

@my_decorator
def my_function():
    print "I'm the function!"

my_function()

#----------------------------
# More complex decorator
#----------------------------

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print "In the decorator!"
            if number == 56:
                print "Not running the function"
            else:
                func(*args, **kwargs)
            print "After the decorator!"
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(53)
def my_function_too(x, y):
    print x + y

my_function_too(10, 17)
