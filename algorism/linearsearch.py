# 線形探索

def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0, 100)
print(ss(numbers, 2))
print(ss(numbers, 200))

