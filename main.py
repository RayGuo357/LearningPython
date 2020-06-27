num = []

def sum(x):
    result = 0
    for y in x:
        result += y
    return result

while True:
    temp = input("Enter a number or 'sum' to sum up your numbers: ")
    if(temp == sum):
        break
    else:
        num.append(temp)

print(sum(num))
