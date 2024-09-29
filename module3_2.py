def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    recipiet_list = []
    recipiet_list.extend(recipient)
    recipient_number = len(recipient)
    # print("Recipient lenth=",recipient_number)
    # print(recipiet_list)
    # print("-1 -2-3-4",recipiet_list[:recipient_number-4:-1])
    # print("-1 -2-3-4", recipiet_list[:recipient_number-4:-1])
    if "@" not in recipiet_list:
        print("1Невозможно отправить письмо с адреса:", sender, "на адрес", recipient)
        return
    # print("10",recipiet_list[:recipient_number-4:-1] != ["u", "r", "."])
    # print("11",recipiet_list[:recipient_number-4:-1] != ["u", "r", "."] or print(recipiet_list[:recipient_number-4:-1] != ["t", "e", "n"]) or recipiet_list[:recipient_number-4:-1] != ["m", "o", "c"])
    # print("12", recipiet_list[:recipient_number - 4:-1] != ["t", "e", "n"])
    # print("13", recipiet_list[:recipient_number - 4:-1] != ["m", "o", "c"])
    if recipiet_list[:recipient_number-4:-1] != ["u", "r", "."] and recipiet_list[:recipient_number-4:-1] != ["t", "e", "n"] and recipiet_list[:recipient_number-4:-1] != ["m", "o", "c"]:
        print("2Невозможно отправить письмо с адреса:", sender, "на адрес", recipient)
        return
    else:
        if sender == recipient:
            print("3Нельзя отправить письмо самому себе")
            return
        if sender == "university.help@gmail.com":
            print(f"4Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
            return
        print(f"5НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
send_email("Hello", "s", sender="d")
print(1)
send_email("dddd", "e@.ru")
print(2)
send_email("help", "ru@mail.net")
print(3)
send_email("hy","university.help@gmail.com")
print(4)
send_email("hy","for@mail.ru", sender = "sdf@ddf.ru")