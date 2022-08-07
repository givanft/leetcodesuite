def is_polidrome(x):
    if x < 0:
        return False

    base = 1
    copy_x = x
    while copy_x > 10:
        copy_x /= 10
        base *= 10
    
    result = 0
    copy_x = x
    while copy_x > 0:
        div = int(copy_x / 10)
        rem = copy_x % 10
        
        result += rem * base
        
        base = int(base / 10)
        copy_x = div
    
    if x == result:
        return True
    
    return False


x = 123454321
print(is_polidrome(x))