def is_armstrong_number(number):
    str_num = str(number)
    num_of_digits = len(str_num)
    result = 0
    for n in str_num:
        result += int(n) ** num_of_digits
    return result == number
