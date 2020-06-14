def fibo_exponential(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

def fibo_linear(n):
    List = [0]*3
    List[0] = 0
    List[1] = 1
    for i in range(2,n+1):
        List[2] = List[1] + List[0]
        List[0] = List[1]
        List[1] = List[2]
    return List[2]

from timeit import timeit

def time():
    print(timeit('fibo_linear(10)', 'from __main__ import fibo_linear', number=100000))
    print(timeit('fibo_exponential(10)', 'from __main__ import fibo_exponential', number=100000))

time()