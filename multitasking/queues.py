import queue
import threading
from time import sleep

tasks_queue = queue.Queue()
task_results_queue = queue.Queue()

"""# send task requests to the worker - nothing will happen until workers start running. The tasks are stored in the queue for now"""
for item in range(10):
    print(f"Create a new task with {item}")
    tasks_queue.put(item)
print('All task requests were sent\n', end='')
print('-' * 100)


def worker():
    """
    This function acts as a worker that accepts a raw argument, and computes a new value with it.
    After computing, it will send it to the results queue
    """
    thread_name = threading.current_thread().name
    while True:
        print(f'{thread_name} awaiting tasks')
        current_item = tasks_queue.get()
        print(f'{thread_name} Working on {current_item}')
        sleep(3)
        computed_value = current_item * current_item
        task_results_queue.put(computed_value)
        print(f'{thread_name} Finished {current_item}')
        tasks_queue.task_done()


def handle_result():
    """
    A worker function that waits for new results to enter the queue, and uses each result
    """
    while True:
        current_item = task_results_queue.get()
        print("Result", current_item)
        task_results_queue.task_done()
        print('-' * 100)


"""
A daemon thread(also called a non-blocking thread) is a thread that dies whenever the main thread dies.
Meaning, the while loop inside will break since the program exits
"""
threads = [
    threading.Thread(name="w1", target=worker, daemon=True),
    threading.Thread(name="w2", target=worker, daemon=True),
    threading.Thread(name="w3", target=worker, daemon=True),
    threading.Thread(name="results_printer", target=handle_result, daemon=True)
]
for t in threads:  # start all threads
    t.start()

"""# block until all tasks are done"""
print("Waiting for tasks to to complete")
print('-' * 100)

tasks_queue.join()
task_results_queue.join()
print('All work completed')
