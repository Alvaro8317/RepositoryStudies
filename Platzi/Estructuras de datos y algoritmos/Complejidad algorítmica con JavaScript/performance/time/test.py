import time


def count_numbers(numbers: int) -> None:
    for i in range(numbers):
        pass


total_time = 0
iterations = 10000  # Número de iteraciones

for _ in range(iterations):
    start_time = time.perf_counter()
    count_numbers(5)
    end_time = time.perf_counter()
    total_time += (end_time - start_time) * 1000  # Convertir a ms

average_time = total_time / iterations
print(f"Average time per execution: {average_time:.6f} ms")
