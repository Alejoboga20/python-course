from time import time
from functools import wraps

def performance(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        
        print(f"time1 {t1}, time2 {t2} ")
        print(f"Time passed: {t2 - t1}s ")
        return result
        
    return wrapper
    
@performance
def long_time():
    for i in range(100000000):
        result = i*i
        
long_time()