# 텍스트 파일에서 가장 긴 단어 출력하기
def strsort():
    with open("word.txt", "w") as file:
        while True:
            user_info = input("Enter the Word> ")
            if not user_info:
                break
            file.write(user_info + "\n")

    with open("word.txt", "r") as file:
        output = [line.strip() for line in file]
        return max(output, key = len)

print(strsort())