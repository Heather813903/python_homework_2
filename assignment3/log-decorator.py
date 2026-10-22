# Task 1

import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):  
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {args if args else'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper

@logger_decorator
def say_hello():
        print("Hello, World!")

@logger_decorator
def check_args(*args):
     return True

@logger_decorator
def check_kwargs(**kwargs):
    return logger_decorator

say_hello()
check_args("apple","banana","cherry")
check_kwargs(name="Heather", role="Flight Attendant")



