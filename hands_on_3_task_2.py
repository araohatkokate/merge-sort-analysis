import time
import matplotlib.pyplot as plt

def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x += 1

# Measure execution time for various values of n
ns = range(1, 1000, 50)
times = []

for n in ns:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times.append(end_time - start_time)

# Plot time vs n
plt.plot(ns, times, label='Execution Time')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Execution Time of f(n) vs n')
plt.legend()
plt.show()
