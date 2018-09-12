def facto(x):
    if x == 1:
        return 1
    return x * facto(x-1)

print(facto(11))
