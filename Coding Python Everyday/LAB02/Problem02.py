# 숫자 더하기

def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

def to_int(number):
    return int(number)

numbers = list(input("Enter the numbers > "))
numbers = map(to_int,numbers)
print(mysum(*numbers))