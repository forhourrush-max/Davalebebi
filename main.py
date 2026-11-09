number= int(input("Enter a number: "))

if number % 2 == 0:
    print(number, 'even')

else:
    print(number, 'odd')


age1 = int(input("Enter Your Age: "))

if age1 <= 12:
    print(age1,'- ' 'Child')

elif 13 <= age1 <= 17:
    print(age1,'- ' 'Teenager')

elif 18 <= age1 <= 64:
    print(age1,'- ' 'Adult')

elif age1 > 64:
    print(age1,'- ' 'Senior')

else:
    print('Invalid Age')


Grade = int(input('Enter Grade: '))

if Grade <0 or Grade > 100:
    print('Invalid Grade')

elif Grade >=90:
    print('A')

elif Grade >=80:
    print('B')

elif Grade >=70:
    print('C')

elif Grade >=60:
    print('D')

elif Grade >=50:
    print('E')

else:
    print('F')


Question = input("Do You Like Python? yes/no: ").lower()

if Question == "yes":
    print('Great!')

elif Question == "no":
    print('Maybe You Will Like It Later')

else:
    print ('Please Answer Yes or No')


first_number = float(input("Enter first number: "))
enter_operation = input("Enter operation: ")
second_number = float(input("Enter second number: "))

if enter_operation == "+":
    result = first_number + second_number
    print(f'{first_number} + {second_number} = {result}')

elif enter_operation == "-":
    result = first_number - second_number
    print(f'{first_number} - {second_number} = {result}')

elif enter_operation == "*":
    result = first_number * second_number
    print(f'{first_number} * {second_number} = {result}')

elif enter_operation == "/":
    result = first_number / second_number
    print(f'{first_number} / {second_number} = {result}')





