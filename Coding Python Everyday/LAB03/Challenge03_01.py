# 부동소수점의 출력

def my_num(f,before,after):
    int_part = int(f)
    float_part = f - int_part

    result_int_part = int_part % (10**before)
    result_float_part = int(float_part * (10**after)) * (10**(-after))
    result = result_int_part + result_float_part

    print(result)

my_num(1234.5678,3,4)