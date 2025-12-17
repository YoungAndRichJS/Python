# 짝수와 홀수의 합 리스트 
def even_odd_sums(sequence):
    even_sum = 0
    odd_sum = 0
    for number in sequence:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    return [odd_sum, even_sum]

print(even_odd_sums([1,2,3,4,5,6]))
print(even_odd_sums((1,2,3,4,5,6)))