import os
from multiprocessing import Process

# each process will have its own list
output = []


def square_numbers(*, proc_id):
    for i in range(1000):
        result = i * i
        x.append(result)
    print('proc ', proc_id, x)


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers, kwargs={'proc_id': i})
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        process.join()
    print()