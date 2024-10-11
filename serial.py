import time
from timefun import timeconsumingfun

if __name__==  '__main__':
    n = 100
    start_time = time.time()
    for i in range(n):
        timeconsumingfun(i)
    finish_time = time.time()

    execution_time = finish_time -  start_time
    print(f"Execution time: {execution_time:.4f} seconds")





