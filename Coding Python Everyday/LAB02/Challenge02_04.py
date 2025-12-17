# 여러 자료형으로 구성된 리스트에서
# 숫자로 변환하여 더하기

def my_list(the_list):
    output = 0
    for element in the_list:
        print(f"현재의 요소의 자료형은 {type(element)}입니다.")
        try:
            output += element
        except:
            if type(element) != int:
                print("현재의 요소는 int 자료형이 아닙니다.")
                if type(element) == str:
                    try:
                        output += int(element)
                        print("int 자료형으로 변환할 수 있습니다.")
                    except ValueError:
                        print("int 자료형으로 변환할 수 없습니다.")
                else:
                    print("int 자료형으로 변환할 수 없습니다.")
    return output

various_type = [1,2,"3","안녕",False,"4",5]
print(f"리스트 안의 숫자들의 총합: {my_list(various_type)}")