import time

print("\n----------Without Multithreading:-----------\n")

def calc_squares(nums):
    print('calculating squares...')
    result = []
    for n in nums:
        time.sleep(0.01)
        result.append(n**2)
        #print('square:', n**2)
    print('sqiuares:', result)

def calc_cubes(nums):
    print('calculating cubes...')
    result = []
    for n in nums:
        time.sleep(0.01)
        result.append(n**3)
        # print('cube:', n**3)
    print('cubes:', result)

numbers = [0, 1, 2, 3]

t = time.time()
calc_squares(numbers)
calc_cubes(numbers)
print('time elapsed:', time.time() - t)

print("\n----------With Multithreading:-----------\n")
import threading

t = time.time()

t1 = threading.Thread(target=calc_squares, args=(numbers, ))   # create a thread, pass args as a tuple
t2 = threading.Thread(target=calc_cubes, args=(numbers, ))     # create a thread, pass args as a tuple
t1.start()      # start the threads
t2.start()
t1.join()       # wait until t1 is done
t2.join()       # wait until t2 is done

print('time elapsed:', time.time() - t)



print("\n----------Locks and Shared Variables:-----------\n")
from queue import Queue

print_lock = threading.Lock()               # create a lock to lock printing -

def example_job(worker):                    # a job to do for every worker
    time.sleep(0.5)                         # waste some time
    with print_lock:                        # you can't perform whatever is beneath unles what is beneath is unlocked by print_lock
        print(threading.current_thread().name, worker)          # print whose doing what

def threader():                             # actual threading operation
    while True:                             # continue going on untill all threads die (daemon dies)
        worker = q.get()                    # take the worker from the queue
        example_job(worker)                 # put worker to work
        q.task_done()                       # thread is complete, move on


q = Queue()

for x in range(10):                         # how many threads (workers) are we going to allow? - 10
    t = threading.Thread(target=threader)   # create a thread 't' for every worker
    t.daemon = True                         # clasify 't' as a daemon so it dies when the main thread dies (is False by default)
    t.start()                               # start the threading

start_time = time.time()                     # we want to keep track of time so let's start counting here

#now assign some jobs:
for worker in range(20):                    # for any variable (called worker) and in range of 20 instances of worker
    q.put(worker)                           # put worker to work

q.join()                                    # wait for the thread to terminate

print('Entire job took:', time.time() - start_time, 's')

# in summary this means 10 Threads doing 20 jobs, each job takes 0.5s
# normally this would take 20 * 0.5s = 10s
# with multithreading it takes less - each one of 10 threads had to do 2 jobs to finish all...
# 2 jobs take 2*0.5s = 1s to finish. Threads started working simultaniously on their jobs, so the whole task was finished in about 1s.