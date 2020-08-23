def trapezoidal(f, a, b, n):
    if n <= 0:
        raise ValueError("You typed n <= 0")

    result = 0
    for i in range (0, n, 1):
        num = a + (i * (b - a)) / n
        if i == 0 or i == n:
            result += f(num)
        else:
            result += 2 * f(num)

    result *= (b - a) / (2 * n)
    return result

import math
import sage
f = lambda x : math.sin(math.radians(x)) / x
print(trapezoidal(f, 1, 3, 6))