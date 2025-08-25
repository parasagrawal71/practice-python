import threading
import time

def worker(name):
    print(f"{name} starting")
    time.sleep(2)
    print(f"{name} finished")

print("\n")
# Create threads
t1 = threading.Thread(target=worker, args=("Thread-1",))
t2 = threading.Thread(target=worker, args=("Thread-2",))

t1.start() # start execution
t2.start()

t1.join() # wait for thread to finish
t2.join()

print("All threads completed")


"""
🔹 Multithreading in Python

🔹 But… The GIL (Global Interpreter Lock)
- Python (CPython implementation) has a Global Interpreter Lock (GIL).
- Only one thread can execute Python bytecode at a time within a single process.
- This means:
    - I/O-bound tasks (waiting on files, network, DB, APIs) → ✅ Multithreading helps because threads can run while others are waiting.
    - CPU-bound tasks (math-heavy, data processing) → ❌ Multithreading doesn’t give true parallelism because of the GIL.

🔹 Workarounds for CPU-bound tasks
- multiprocessing module → spawns separate processes, each with its own Python interpreter and GIL. True parallelism on multiple cores.
- C extensions / NumPy → heavy lifting done in C (releases the GIL).
- AsyncIO → for concurrent I/O without threads.

🔹 Key Concepts in Python threading
- threading.Thread(target=func, args=()) → create a thread.
- .start() → start execution.
- .join() → wait for thread to finish.
- threading.Lock() → synchronization to prevent race conditions.
- threading.current_thread() → get current thread.

"""

# ################################################################

from multiprocessing import Process, cpu_count
import os

def square(n):
    print(f"Process {os.getpid()} computing square of {n}")
    return n * n

# How to run this?
if __name__ == "__main__":
    numbers = [1, 2, 3, 4]

    processes = []
    for num in numbers:
        p = Process(target=square, args=(num,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed")


# ################################################################


import asyncio
import time

async def worker(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)   # non-blocking sleep
    print(f"{name} finished after {delay} seconds")
    return f"{name} result"

async def main():
    start = time.time()

    # Run tasks concurrently
    tasks = [
        asyncio.create_task(worker("Task-1", 2)),
        asyncio.create_task(worker("Task-2", 3)),
        asyncio.create_task(worker("Task-3", 1)),
    ]

    results = await asyncio.gather(*tasks)
    print("Results:", results)

    print(f"Total time: {time.time() - start:.2f} seconds")

asyncio.run(main())

print("\n")