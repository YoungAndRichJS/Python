# 부동소수점 계산을 정확하게 할 수 있는 Decimal 클래스
# 부동소수점의 계산을 정확하게 하기
from decimal import Decimal

number1, number2 = input("Enter 2 numbers> ").split(" ")
print(Decimal(number1) + Decimal(number2))
