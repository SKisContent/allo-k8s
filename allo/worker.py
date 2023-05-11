import random
import time
import sys
import os
import requests

def numbers(a,b):
    return(i for i in range(a,b))

def linear_sum(a):
    return(sum(numbers(a[0],a[1])))

# get environment value for endpoint
SLEEP_SERVICE = os.environ.get('SLEEP_SERVICE', 'http://localhost:8080/sleep/')

# this function loops forever and calls the sleep service
def do_work(sleep_time, run_time):
    start_time = time.time()
    while True:
        current_time = time.time()
        print("Running time: {}".format(current_time - start_time))
        if current_time - start_time >= run_time:
            print("Sleeping for {} seconds".format(sleep_time))            
            resp = requests.get(SLEEP_SERVICE + str(sleep_time))
            start_time = time.time()
        n = random.randint(0, 2000)
        sum = linear_sum([0, n+1])
        # print(sum)

if __name__ == "__main__":
    sleep_time = float(sys.argv[1])
    run_time = float(sys.argv[2])
    do_work(sleep_time, run_time)
