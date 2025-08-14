



import math

_1_50 = 1 << 50  # 2**50 == 1,125,899,906,842,624

def isqrt(x):
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    if x < _1_50:
        return int(math.sqrt(x))  # use math's sqrt() for small parameters
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr

for _ in range(int(input())):
    x = int(input())

    print(int((isqrt(1+8*x)/2 - 1/2)))

    # need O(1) algorithm to calculate the answer
    # find a fast estimation square root problem and estimate?
    # find the biggest n such that (n)(n+1)/2 <= k where k is the input number

    # n(n+1)/2 = k -- then round down afterwards
    # n^2 + n = 2k

    # n^2 + n - 2k = 0

    # n = -1/2 + (sqrt(1 + 8k))/2 then round down