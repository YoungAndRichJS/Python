# 숫자들의 평균 계산 함수 만들기

def my_sum(numbers):
    output = 0
    for number in numbers:
        output += number
    return output

def average(numbers):
    return my_sum(numbers) / len(numbers) 

def to_int(number):
    return int(number)

# numbers = list(input("Enter the numbers > "))
# numbers = list(map(to_int,numbers))
# print(f"Average : {average(numbers)}")


user_input = input("Enter the numbers > ")
numbers = [to_int(number) for number in user_input.split(" ")]
print(f"Average : {average(numbers)}")