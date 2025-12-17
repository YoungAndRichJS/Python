# 달린 시간 계산하기
def run_timing():
    run_frequency = 0
    run_sum = 0
    while True:
        user_time = input("Enter 10 km run time: ")
        try:
            user_time = float(user_time)
            run_frequency += 1
            run_sum += user_time
        except:
            if user_time == "":
                run_average = float(run_sum / run_frequency)
                print(f"\nAverage of {run_average}, over {run_frequency} runs")
                break
            else:
                raise ValueError
        
run_timing()