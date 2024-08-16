def send_email(message, recipient, *,sender="university.help@gmail.com"):
    end_=[ ".com",".ru",".net"]
    is_b= False
    is_end_r = False
    is_end_s = False
    for i in end_:
        if recipient[len(recipient) - len(i):len(recipient) + 1] == i:
            is_end_r = True
            break
    for j in end_:
        if  sender[len(sender) - len(j):len(sender)+1] == j:
            is_end_s = True
            break
    if '@' in recipient and '@' in sender:
        is_b= True
    if (is_b and is_end_s and is_end_r) ==False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')