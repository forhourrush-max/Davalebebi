# num = 1
#
# while num <= 50:
#     if num % 2 == 0:
#         print(num)
#     num += 1


# N = int(input('Enter a number: '))
# num = 1
# total = 0
# while num <= N:
#     total += num
#     num += 1
#
# print('sum:', total)


# N = int(input('Enter a number: '))
# num = 1
# total = 1
# while num <= N:
#     total *= num
#     num += 1
#
# print(f'{N}! = {total}')



# num = 0
# total = 0
#
# number = int(input('Enter a number: '))
# while number != 0:
#     num += 1
#     total += num
#     number = int(input('Enter a number: '))
#
# print('num: ',number)
# print('Sum: ',total)
#
# if num>0:
#     average = total/num
#     print('The average is: ',average)
# else:
#     print('The average is: ',0)


# secret = 10
# attempts = 5
# count = 0
# correct = False
#
# while count < attempts and not correct:
#     guess = int(input("Guess: "))
#     count += 1
#
#     if guess > secret:
#         print("Too high")
#     elif guess < secret:
#         print("Too low")
#     else:
#         print("You win!")
#         guessed_correctly = True
#
# if not correct:
#     print('You lose! The number was 10')