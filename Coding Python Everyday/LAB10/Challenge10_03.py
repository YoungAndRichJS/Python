# 리스트 안의 합을 기준으로 정렬하는 함수
def sum_list(*number_list):
    output = sorted(number_list, key= mysum)
    return ", ".join([str(number) for number in output])

def mysum(numbers):
    if not numbers:
        return 0
    return sum(numbers)

print(sum_list([], [1,2,3,4,5], [1,2,3,4], [1,2,3], [1,2], [1]))