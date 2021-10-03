n = int(input("How many sets of lottery numbers to generate: "))

import random
lotteryNumbers = []
for i in range(0,7):
  number = random.randint(1,40)
  while number in lotteryNumbers:
    number = random.randint(1,40)
  lotteryNumbers.append(number)
lotteryNumbers.sort()

for i in range(n):
  while number in lotteryNumbers:
    number = random.randint
  print (lotteryNumbers)