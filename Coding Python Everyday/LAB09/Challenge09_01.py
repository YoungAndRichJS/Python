# 첫 번째 요소 보다 큰 것들만 더하기
def mysum_bigger_than(standard, *items):
    if not items:
        return items
    output = type(standard)()
    for item in items:
        if item > standard:
            output += item
    return output
            
print(mysum_bigger_than(10, 5, 20, 30, 6))