# 5764801
mod = 20201227
target = 5764801
target = 17807724


x = 1
mult = 7
loops = 0
while x != target:
    x *= mult
    x = x % mod
    loops += 1

print(loops, x)



mod = 20201227
card_key = 335121
card_loop = 8156519
door_key = 363891
door_loop = 5062092

x = 1
for _ in range(door_loop):
    x *= card_key
    x %= mod

y = 1
for _ in range(card_loop):
    y *= door_key
    y %= mod


print(x, y)


# try 1: 12909639 -- too high
# try 2: 9420461 -- one gold star!
