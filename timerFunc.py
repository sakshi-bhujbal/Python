import random as rand
import time

def repeat(times):
    def decorator(add):
        def wrapper(*args):
            print("The processing has started")
            start = time.time()
            print("Start time",start)
            for i in range (times):
                add(*args)
                time.sleep(3)
                print("The processing has stopped")
                print("end time",time.time())
        return wrapper
    return decorator


@repeat(5)
def add(a,b):
    a = rand.randint(1,10)
    print(f"{a} + {b} = ",a + b)


add(3,5)