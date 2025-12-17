# 파일에서 단어 정렬 후 마지막 단어 출력하기

def wordsort():
    with open("word.txt", "w") as file:
        while True:
            user_info = input("Enter the Word> ")
            if not user_info:
                break
            file.write(user_info + "\n")
    
    with open("word.txt", "r") as file:
        word_list = [line.strip() for line in file]
        return sorted(word_list)[-1]

print(wordsort())