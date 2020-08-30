# Simple code to approximate integrals
# using simpson's approach. This example
# is on the function: f(x) = 1 / (x+1), [1, 2]
# for n = 3 and becomes 2*n
# By: Gkountelos Dimitrios

def simpson(f, a, b, n):
    if n <= 0:
        raise ValueError("you typed wrong number")

    result = 0
    x = 0
    # i use 2*n, because it
    # needs to be even number
    for i in range (0, 2*n+1, 1):
        x = a + i * (b-a) / (2*n)
        if i==0 or i==2*n:
            result += f(x)
        elif i % 2==1:
            result += 4*f(x)
        else:
            result += 2*f(x)

    result *= (b-a) / (6*n)
    return result

f = lambda x : 1 / (x+1)
print(simpson(f, 1, 2, 3))