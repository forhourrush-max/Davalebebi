# def print_ticket(passenger, destination, ticket):
#   print("---------_----TICKET-----------------")
#   print(f"Passenger: {passenger}")
#   print(f"Destination: {destination}")
#   print(f"Class: {ticket}")
#
# print_ticket('Nika', 'Batumi', 'economy' )
# print_ticket(destination='Kutaisi', passenger= 'Mari', ticket = 'Business')
# print_ticket('Nika', 'Tbilisi', ticket = 'Economy')


# def celsius_to_fahrenheit(celsius):
#   return celsius * 9 / 5 + 32
#
# f_0 = celsius_to_fahrenheit(0)
# f_37 = celsius_to_fahrenheit(37)
# f_100 = celsius_to_fahrenheit(100)
# print(f'0c = {f_0}f')
# print(f'37c = {f_37}f')
# print(f'100c = {f_100}f')
#
# def is_warm(celsius, limit=20)
#     return celsius > limit
#
# print(is_warm(25))
# print(is_warm(25,30))
# print(is_warm(limit=10, celsius=25)

# def analyze_numbers(numbers)
#     smallest = min(numbers)
#     largest = max(numbers)
#     av = sum(numbers) / len(numbers)
#     return smallest, largest, average
#
# nums = [12, 7, 25, 3, 18]
#
# minimum, maximum, average = analyze_numbers(nums)
# print(minimum, maximum, average)
#
# result_tuple = analyze_numbers(nums)
# print(result_tuple)

# def add_student(name, group=None):
#     if group is None:
#         group = []
#     if name not in group:
#         group.append(name)
#     return group
#
# group_a = add_student('Ana')
# group_a = add_student('Mari', group_a)
# group_a = add_student("Nika", group_a)
# group_b = add_student('John')
#
# print("group_a:", group_a)
# print("group_b:", group_b)


def check_password(password):
    if len(password) < 6:
        return 'Too Short'
    if password.isdigit():
        return 'Weak'
    if not any(a.isdigit() for a in password) or not any(a.isalpha() for a in password):
        return 'Medium'
    return 'Strong'

password = ['abc', '1234567', 'qwerty', 'python3', 'Tbilisi123']

for l in password:
    rating = check_password(l)
    print(f'{l} --> {rating}')