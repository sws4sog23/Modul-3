def get_multiplied_digits(number):
    str_number = str(number)
    str_number = str_number.replace('0', '')
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    for i in range(len(str_number)):
        if i < len(str_number):
            return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(1023006)
print(result)
