# numbers = [4, 8, 15, 8, 16, 23, 4, 42, 15, 8]
# unique = list(set(numbers))
# print('List Without Duplicates:', unique)
#
# print('Amount:', len(unique))
#
# print(23 in unique)

# ana = {'python', 'java', 'c', 'sql'}
# nika = {'python', 'javascript', 'sql', 'go'}
#
# both = ana | nika
# both1 = ana.union(nika)
# print(both)
# print(both1)
#
# same = ana & nika
# same1 = ana.intersection(nika)
# print(same)
# print(same1)
#
# diff = ana - nika
# diff1 = ana.difference(nika)
# print(diff)
# print(diff1)
#
# sym = ana ^ nika
# sym1 = ana.symmetric_difference(nika)
# print(sym)
# print(sym1)

# votes = ['Ana', 'Nika', 'Ana', 'Mari', 'Nika', 'Ana', 'Mari', 'Ana']
#
# vote = {}
#
# for name in votes:
#     if name in vote:
#         vote[name] += 1
#     else:
#         vote[name] = 1
#
# for name, count in vote.items():
#     print(f'{name}: {count}')


# inventory = {
#     'laptop': {'price': 2500, 'quantity': 5},
#     'mouse': {'price': 40, 'quantity': 0},
#     'keyboard': {'price': 120, 'quantity': 12},
#     'monitor': {'price': 800, 'quantity': 0},
# }
#
# value = 0
# for items, inv in inventory.items():
#     value += inv['price'] * inv['quantity']
# print(value)
#
# print('0 quantity')
# for item, inv in inventory.items():
#     if inv['quantity'] == 0:
#         print(item)
#
# name = input('Enter Product Name: ').lower()
# quantity1 = int(input('Enter Quantity: '))
#
# if name not in inventory:
#     print('Product Not Found')
# elif inventory[name]['quantity'] < quantity1:
#     print('Not Enough')
# else:
#     inventory[name]['quantity'] -= quantity1
#     cost = inventory[name]['price'] * quantity1
#     print(f"Cost: {cost}")
#     print(f'Left ({inventory[name]['quantity']})')


# words = ['python', 'java', 'ai', 'sql', 'go', 'python']

# square = [x**2 for x in range(1,11)]
# print(square)

# length = {word: len(word) for word in words}
# print(length)

# first_letters = {word[0] for word in words}
# print("First letters:", first_letters)