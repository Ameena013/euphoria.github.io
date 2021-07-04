import random
count = 0
sum = 0
dices = []
while sum < 50:
    dice = random.randrange(1, 7)
    dices.append(dice)
    sum = sum + dice
    count= count + 1

print("Roll:",dices)
print("Count:",count)


