# 식당 주문 프로그램 만들기

MENU = {
    "sandwich": 10,
    "tea": 7,
    "coffee": 5
}

def restaurant():
    total_price = 0

    while True:
        order_for_counter = input("Order: ")
        if order_for_counter == "":
            finish_order(total_price)
            break
        else:
            total_price = custumer(order_for_counter, total_price)
    return 

def custumer(order_for_counter, total_price):
    if order_for_counter in MENU:
        total_price += MENU[order_for_counter]
        print(f"{order_for_counter} costs {MENU[order_for_counter]}, total is {total_price}")
        return total_price
    else:
        print(f"Sorry, we are fresh out of {order_for_counter} today.")
        return total_price

def finish_order(total_price):
    print(f"Your total is {total_price}, Thank you!")
    
restaurant()