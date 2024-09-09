# Merge Sort Analysis
## Overview
This assignment focuses on analyzing the time complexity of a function with two nested loops that each run \(n\) times, resulting in a complexity of **O(n²)**. There is also measurement of the function’s execution time for various input sizes, plot the results, and fitting a polynomial curve to verify the quadratic time complexity. The plot graph also determines \(n_0\), the point where the function's asymptotic behavior begins to dominate.There is also implementation of Merge Sort, which runs in **O(n log n)**.


## Time Complexity Analysis (Task 3)

### Big-O (Upper Bound)
Since the time complexity grows quadratically, the upper bound is **O(n²)**. This means the function's runtime will not grow faster than **n²** as **n** increases.

### Big-Omega (Lower Bound)
The function executes at least **n²** operations, so the lower bound is **Ω(n²)**.

### Big-Theta (Tight Bound)
Since both the upper and lower bounds are **n²**, the tight bound is **Θ(n²)**.

## Function modification and runtime impact (Task 4 and 5)
Yes, it will slightly increase the runtime because an extra operation `y = i + j` is added to each iteration. However, this is still a constant-time operation, so the overall time complexity remains **O(n²)**. The actual runtime will increase, but the growth rate will not change.

No, the results from #1 are based on the asymptotic behavior of the algorithm, and since adding `y = i + j` is just an additional constant-time operation, it does not change the time complexity from **O(n²)**.

