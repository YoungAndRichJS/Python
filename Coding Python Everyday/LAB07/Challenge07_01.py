# 단어별로 알파벳 정렬하여 출력하기

def strsort(sentence):
    output = []
    word_list = sentence.split(" ")
    for word in word_list:
        letter = sorted(word.lower())
        output.append(",".join(letter))
    return output

print(strsort("Tom Dick Harry"))