def solution(slice, n):
    x = n // slice
    if n % slice != 0:
        return x + 1
    else:
        return x