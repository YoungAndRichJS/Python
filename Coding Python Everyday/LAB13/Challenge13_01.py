# 로그인

ID_AND_PASSWORD = {
    "Hanjs": "asdf1234",
    "Hanas": "qwerasdf1234",
    "Hanbs": "asdfqwer"
}

def login():
    user_id = input("Enter you ID >> ").strip()
    if user_id in ID_AND_PASSWORD:
        user_password = input("Enter your password >> ").strip()
        if ID_AND_PASSWORD.get(user_id) == user_password:
            print("로그인 성공!")
            return

    print("로그인 실패")

login()