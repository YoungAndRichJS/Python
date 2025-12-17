# 더하고 빼고의 반복
def plus_minus(sequence):
    output = sequence[0]
    change_turn = True
    for number in sequence[1:]:
        if change_turn:
            output += number
        else:
            output -= number
        change_turn = not change_turn
    return output


print(plus_minus([10,20,30,40,50,60]))
print(plus_minus((10,20,30,40,50,60)))