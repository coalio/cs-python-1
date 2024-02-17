def fibonacci(n: int):
    """
    Calculates the fibonacci sequence up to N
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    