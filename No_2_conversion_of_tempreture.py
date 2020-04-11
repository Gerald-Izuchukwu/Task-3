user_temp = input(
    "Please enter the tempreture you'd like to convert(e.g., 45F, 102C etc.): ")
degree = int(user_temp[:-1])
input_convention = user_temp[-1]

if input_convention.upper() == "C":
    result = int(float((9 * degree) / 5 + 32))
    output_convention = "Fahrenheit"
elif input_convention.upper() == "F":
    result = int(float((degree - 32) * 5 / 9))
    output_convention = "Celsius"
else:
    print("Input proper convention.")
    quit()
print(f"The temperature in {output_convention}, is {result} degrees.")
