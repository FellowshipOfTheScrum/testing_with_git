def fibo(x):
    if x == 1:
        return 1
    if x == 0:
        return 0
    return fibo(x-1) + fibo(x-1)

print(fibo(3))
