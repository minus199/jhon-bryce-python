import os

from time import sleep

# example of fork/waitpid
# pid is process id - the id of the process given by the os
for i in range(2):
    print(f"{i} I am {os.getpid()} and I'm about to be a dad!")
    sleep(3)
    pid = os.fork()
    curr_pid = os.getpid()
    print('-' * 10)
    if pid == 0:
        print(f"{i} I'm {curr_pid}, a newborn that knows to write to the terminal!")
    else:
        print(f"{i} I am {curr_pid} and I'm the dad of {pid}, and he knows to use the terminal!")
        os.waitpid(pid, 0)
    print('-' * 10)

