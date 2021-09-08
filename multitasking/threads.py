import time
from threading import Thread, Lock


def myfunc(*args):
    print("From thread", args)
    time.sleep(5)


th1 = Thread(target=myfunc, args='1')
th2 = Thread(target=myfunc, args='2')
th1.start()
th2.start()
print("From main")
th1.join()
th2.join()


def square_numbers():
    for i in range(1000):
        result = i * i # some heavy computing/processing


threads = []
num_threads = 10

# create threads and asign a function for each thread
for i in range(num_threads):
    thread = Thread(target=square_numbers)
    threads.append(thread)

# start all threads
for thread in threads:
    thread.start()

# wait for all threads to finish
# block the main thread until these threads are finished
for thread in threads:
    thread.join()



