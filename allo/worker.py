import random
import time
import sys

def numbers(a,b):
    return(i for i in range(a,b))

def linear_sum(a):
    return(sum(numbers(a[0],a[1])))


# this function loops forever and randomly sleeps for 0-10 seconds
def do_work(sleep_time, run_time):
    start_time = time.time()
    while True:
        current_time = time.time()
        if current_time - start_time >= run_time:
            print("Sleeping for {} seconds".format(sleep_time))
            time.sleep(run_time)
            start_time = time.time()
        time.sleep(sleep_time)
        n = random.randint(0, 2000)
        sum = linear_sum([0, n+1])
        # print(sum)

if __name__ == "__main__":
    sleep_time = float(sys.argv[1])
    run_time = float(sys.argv[2])
    do_work(sleep_time, run_time)
