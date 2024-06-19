import time

def fibonacci_1(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci_1(n-1) + fibonacci_1(n-2)

def fibonacci_2(n: int) -> int:
    f1: int = 1
    f2: int = 1
    for i in range(n-1):
        (f1, f2) = (f1+f2, f1)
    return f1

def fibonacci_3(n: int) -> int:
    def fibonacci_3_rec(n: int) -> (int, int):
        if n == 0:
            return (1, 1)
        if n == 1:
            return (1, 1)
        (f1, f2) = fibonacci_3_rec(n-1)
        return (f1+f2, f1)
    (f1, f2) = fibonacci_3_rec(n)
    return f1


n: int = 30

start = time.time()
print(fibonacci_1(n))
end = time.time()
print("{:e}".format(end-start))


start = time.time()
print(fibonacci_2(n))
end = time.time()
print("{:e}".format(end-start))

start = time.time()
print(fibonacci_3(n))
end = time.time()
print("{:e}".format(end-start))
