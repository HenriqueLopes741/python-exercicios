def fatorial(a, show=False):
    result = 1

    for c in range(1, a + 1):
        result *= c
        if show:
            print(c, end=' x ' if c < a else ' = ')

    return result

print(fatorial(5, show=False))
