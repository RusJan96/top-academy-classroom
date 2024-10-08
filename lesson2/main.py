


def check(x1: int, x2: int, f1: int, f2: int) -> bool:
    return True if ((x1 + 1 == f1) or (x1 - 1 == f1) or (x1 == f1)) and ((x2 + 1 == f2) or (x2 - 1 == f2) or (x2 == f2)) else False

assert check(4,4,5,5) == True
assert check(4,4,2,5) == False
assert check(1,1,1,2) == True
assert check(4,4,5,5) == True
assert check(5,5,4,3) == False
assert check(3,3,5,4) == False
assert check(4,4,4,5) == True
print("Успешно!")