# 문자열 리스트를 새로운 리스트로 구현

def my_list(the_list):
    output = []
    for word in the_list:
        new_word = list(word.split(" "))
        for i in range(len(new_word)):
            if len(output) <3:
                output.append(new_word[i])
            else:
                output[i] = " ".join([output[i], new_word[i]])
    return output

print(my_list(["abc def ghi", "jkl mno pqr", "stu vwx yz"]))