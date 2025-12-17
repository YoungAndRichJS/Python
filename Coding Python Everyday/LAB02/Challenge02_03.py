# 단어 길이 및 평균 구하기

def word_length(word_list):
    sum_of_word_length = 0
    min_of_word_length = len(word_list[0])
    max_of_word_length = len(word_list[0])

    for word in word_list:
        sum_of_word_length += len(word)
        if len(word) < min_of_word_length:
            min_of_word_length = len(word)
        if len(word) > max_of_word_length:
            max_of_word_length = len(word)
        print(f"{word} : ({len(word)})")
    
    return min_of_word_length, max_of_word_length, sum_of_word_length/len(word_list)

word_list = ["안녕", "하세요",  "반갑습니다", "제", "이름은 한정석입니다"]
min_len, max_len, avg_len = word_length(word_list)
print(f"가장 짧은 단어의 길이 : {min_len}")
print(f"가장 긴 단어의 길이 : {max_len}")
print(f"평균 단어 길이 : {avg_len:.2f}")