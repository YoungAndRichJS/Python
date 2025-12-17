# 숫자 더하기

def mysum(numbers,start):
    output = start
    for number in numbers:
        output += int(number)
    return output

numbers = list(input("Enter the number > "))
start = int(input("Enter the start Number > "))
print(mysum(numbers,start))
