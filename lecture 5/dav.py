from sys import exception

# age = int(input('Enter Your Age :'))
# price = int(input('Enter Money :'))
#
# if age >= 12 and price >= 15 :
#     print('Enjoy The Movie')
#
# else:
#     print('Access Denied')
#


# year = int(input("Enter year: "))
#
# year = year % 4
# year = year % 100
# year = year % 400
#
# if (year % 4== 0 and year % 100 != 0) or (year % 400 == 0):
#     print('leap year')
# else:
#     print('not leap year')


# pin = int(input('Input Your Pin: '))
#
# if pin == 1234:
#
#     money = int(input('Input Amount Of Money To Withdraw: '))
#
#     if money <= 0:
#         print('Invalid Amount')
#
#     elif money > 500:
#         print('Not Enough Money')
#
#     else:
#         new_balance = 500 - money
#         print(f'Get Your Money: {money}')
#         print(f'new balance: {new_balance}')
#
# else:
#     print('Wrong Pin')

try:
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    number = int(input('Enter a number to divide 100 by: '))

    print('100 /', number, '=', 100 / number)
    print(f'Hello, {name} ! Next year you will be {age + 1}  years old.')

except ValueError:
    print('Invalid Input')

except ZeroDivisionError:
    print('Cannot Divide By Xero')

except TypeError:
    print('Cannot Join Text And Number')

except exception as e:
    print(e)

