for number in range(1500, 2700):
    number_list = []
    if number % 7 == 0 and number % 5 == 0:
        number_list.append(number)
        print(number_list)
