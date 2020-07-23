# utils.py
import json
from functools import wraps
import gc
import timeit


def measureTime(f, no_print=False, disable_gc=False):
    """
    decorator to measure time execution
    :param f: the function for which time execution will be measured
    :param no_print:
    :param disable_gc:
    :return:
    """
    @wraps(f)
    def _wrapper(*args, **kwargs):
        gcold = gc.isenabled()
        if disable_gc:
            gc.disable()
        start_time = timeit.default_timer()
        try:
            result = f(*args, **kwargs)
        finally:
            elapsed = timeit.default_timer() - start_time
            if disable_gc and gcold:
                gc.enable()
            if not no_print:
                print('execution time measured for function "{}": {}s'.format(f.__name__, elapsed))
        return result
    return _wrapper


class MeasureBlockTime:
    def __init__(self,name="(block)", no_print=False, disable_gc=False):
        self.name = name
        self.no_print = no_print
        self.disable_gc = disable_gc

    def __enter__(self):
        self.gcold = gc.isenabled()
        if self.disable_gc:
            gc.disable()
        self.start_time = timeit.default_timer()

    def __exit__(self,ty,val,tb):
        self.elapsed = timeit.default_timer() - self.start_time
        if self.disable_gc and self.gcold:
            gc.enable()
        if not self.no_print:
            print('Function "{}": {}s'.format(self.name, self.elapsed))
        return False  # re-raise any exceptions


def object_to_dict(obj):
    """
    :param obj: A class object
    :return: a dictionary representation of class/object variables of an object, there may be nested objects
    """
    if isinstance(obj, (list,set,int,float,str,dict)):
        raise TypeError('Please provide a user defined object instance')
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


def first_common_occurrence(x, y):
    """
    :param x: 1st list
    :param y: 2nd list
    :return: return the first common occurrence between two lists in order else None
    """
    if not isinstance(x, (list,tuple,set)) or not isinstance(y, (list,tuple,set)):
        raise TypeError("please provide two sequence types")
    return next(filter(set(y).__contains__, x), None)





