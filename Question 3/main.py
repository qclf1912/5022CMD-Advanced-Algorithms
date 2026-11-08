"""Command-line runner for Fibonacci concurrency experiment."""

import sys
import threadLib


def main():
    # Get the number of experiment rounds from the command-line argument (default: 10).
    rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    # Compare the average execution time of multithreaded and serial Fibonacci calculations.
    avg_threads = threadLib.run_experiment("With Multithreading", threadLib.run_with_threads, rounds)
    avg_serial = threadLib.run_experiment("Without Multithreading", threadLib.run_without_threads, rounds)

    # Calculate the percentage of execution time reduced by multithreading.
    diff = ((avg_serial - avg_threads) / avg_serial * 100) if avg_serial > 0 else 0.0

    print("\n=== Summary ===")
    print(f"Average with multithreading    : {avg_threads:,} ns")
    print(f"Average without multithreading : {avg_serial:,} ns")

    # Display whether multithreading improved or increased the execution time.
    if diff > 0:
        print(f"Observation: Multithreading reduced the average time by {diff:.1f}%.")
    else:
        print(f"Observation: Multithreading did NOT reduce the time; it was {abs(diff):.1f}% slower.")


# Run the main function only when this file is executed directly.
if __name__ == "__main__":
    main()