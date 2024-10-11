import multiprocessing
import time
from timefun import timeconsumingfun

if  __name__ == '__main__':
    n = 50
    processes = 16

    with multiprocessing.Pool(processes=processes) as pool:
        start_time = time.time()
        pool.map(timeconsumingfun, range(n))
        finish_time = time.time()
        
        elapsed_time = finish_time -  start_time
        print(f"Time taken: {elapsed_time:6f} seconds")
        
