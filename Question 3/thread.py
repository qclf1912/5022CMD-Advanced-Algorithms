"""Custom thread class for concurrent computation."""

import threading
import time


class MyThread(threading.Thread):
    """Custom thread class to compute tasks concurrently."""

    # Initialize the thread with its Fibonacci input and shared result lists.
    def __init__(self, n, index, results, starts, ends):
        super().__init__()
        self.n = n
        self.index = index
        self.results = results
        self.starts = starts
        self.ends = ends

    # Define the task performed when the thread starts.
    def run(self):
        import threadLib

        # Record the execution time before and after the Fibonacci calculation.
        self.starts[self.index] = time.perf_counter_ns()
        self.results[self.index] = threadLib.fibonacci(self.n)
        self.ends[self.index] = time.perf_counter_ns()