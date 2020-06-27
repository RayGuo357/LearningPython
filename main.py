def sum(*list):
    result = 0
    for x in list:
        result += x
    return result

print(sum(2, 5, 13))
