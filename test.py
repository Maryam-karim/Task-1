herd_of_cows = int(input("Enter how many cows are in the herd: "))
unique_3_digit_code_list = []
rounded_yield_list = {}
total_weekly_volume = 0
cows_with_their_corresponding_milk = {}

# Input milk yields for each cow
for i in range(1, herd_of_cows + 1):
    while True:
        unique_3_digit_code = input("Enter the unique 3 digit identity code for cow {}: ".format(i))
        if len(unique_3_digit_code) != 3:
            print("Code is longer or shorter than 3 digits. Please enter a unique 3 digit identity code.")
        elif unique_3_digit_code in unique_3_digit_code_list:
            print("Code already exists. Please enter a unique 3 digit identity code.")
        else:
            unique_3_digit_code_list.append(unique_3_digit_code)
            break

    rounded_yield_list[unique_3_digit_code] = []
    rounded_yield_total = 0

    for day in range(7):
        daily_yield = 0
        for milking in range(2):
            while True:
                try:
                    volume_of_milk = float(input(f"Enter the milk yield of cow {unique_3_digit_code} on day {day+1} of milking {milking+1}: "))
                    if volume_of_milk < 0:
                        print("Yield cannot be negative. Please enter a valid yield.")
                    else:
                        rounded_yield = round(volume_of_milk, 1)
                        rounded_yield_list[unique_3_digit_code].append(rounded_yield)
                        rounded_yield_total += rounded_yield
                        daily_yield += rounded_yield
                        break
                except ValueError:
                    print("Please enter a numeric value.")

    cows_with_their_corresponding_milk[unique_3_digit_code] = rounded_yield_total
    total_weekly_volume += rounded_yield_total

# Check for cows with low yield after collecting all data
for unique_3_digit_code, total_yield in cows_with_their_corresponding_milk.items():
    days_with_low_yield = sum(1 for yield_value in rounded_yield_list[unique_3_digit_code] if yield_value < 12)
    if days_with_low_yield >= 4:
        print("Cow {} has a yield of less than 12 liters of milk for four days or more in the week.".format(unique_3_digit_code))

# Identify cow with the maximum yield
max_yield_cow = max(cows_with_their_corresponding_milk, key=cows_with_their_corresponding_milk.get)
max_yield = cows_with_their_corresponding_milk[max_yield_cow]

# Output results
print(f"The cow with the maximum yield of milk is {max_yield_cow} with a yield of {max_yield}.")
print("Total weekly volume of milk for the herd is", total_weekly_volume)
print("Average yield per cow in a week is", total_weekly_volume / herd_of_cows)
