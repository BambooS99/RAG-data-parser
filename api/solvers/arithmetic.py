def add(numbers:list [int | float]) -> int | float:
    res = 0
    for i in numbers:
        res += i
    return res