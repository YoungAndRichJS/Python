# 절댓값으로 정렬하는 함수 만들기
def mynum(*numbers):
    output = sorted(numbers, key=abs)
    return ",".join([str(number) for number in output])

print(mynum(1,9,-2,-8,7,-5,6,3,4))