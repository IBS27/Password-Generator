import random

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '()[]{},;:.-_/\\?+*# '

upper, lower, nums, syms = True, True, True, True

final = ""

if upper:
    final += uppercase_letters
if lower:
    final += lowercase_letters
if nums:
    final += digits
if syms:
    final += symbols

length = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(final, length))
    print(password)
