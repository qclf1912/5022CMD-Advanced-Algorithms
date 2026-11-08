"""Helper library containing Fibonacci logic, worker thread coordination, and experiment runners."""

import time
from thread import MyThread


# Fibonacci numbers used for both multithreaded and serial experiments.
NUMBERS = (35, 38, 40)


# Calculate Fibonacci numbers using naive recursion.
def fibonacci(n):
    """Naive recursive Fibonacci. Time complexity O(2^n)."""

    # Stop recursion when the input reaches the base cases (0 or 1).
    if n <= 1:
        return n

    # Calculate the current Fibonacci number using the two previous values.
    return fibonacci(n - 1) + fibonacci(n - 2)


# Execute all Fibonacci calculations concurrently using multiple threads.
def run_with_threads():
    results = [None] * len(NUMBERS)
    starts = [0] * len(NUMBERS)
    ends = [0] * len(NUMBERS)

    # Create one thread for each Fibonacci number, sharing the result and timing lists.
    threads = [
        MyThread(n, i, results, starts, ends)
        for i, n in enumerate(NUMBERS)
    ]

    # Start all threads before waiting for them to finish.
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # Measure the total elapsed time from the first thread starting to the last one finishing.
    elapsed = max(ends) - min(starts)
    return results, elapsed


# Execute Fibonacci calculations sequentially without using additional threads.
def run_without_threads():
    start = time.perf_counter_ns()
    results = [fibonacci(n) for n in NUMBERS]
    end = time.perf_counter_ns()

    return results, end - start


# Run the selected experiment multiple times and calculate its average execution time.
def run_experiment(title, runner, rounds):
    print(f"\n=== Fibonacci Computation ({title}) ===")
    times = []

    for r in range(1, rounds + 1):
        results, t = runner()
        times.append(t)

        # Format and display the Fibonacci results and execution time for each round.
        shown = ", ".join(f"Fib({n})={v}" for n, v in zip(NUMBERS, results))
        print(f"Round {r:<2}: {shown} | T = {t:,} ns")

    # Calculate the average execution time across all experiment rounds.
    average = sum(times) // len(times)
    print(f"Average T ({title}): {average:,} ns")

    return average