import random

uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase_letters = uppercase_letters.lower()
digits = "1234567890"
symbols = "()[]{},.;:-_/\?+*#@!$%&* "

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 12
amount = 1

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)