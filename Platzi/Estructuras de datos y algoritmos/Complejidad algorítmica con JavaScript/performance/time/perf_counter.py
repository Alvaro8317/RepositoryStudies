import time


def count_numbers(numbers: int) -> None:
    for i in range(numbers):
        pass


start_time = time.perf_counter()
count_numbers(5)
end_time = time.perf_counter()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Time taken: {elapsed_time_ms:.3f} ms")
