def lottery(lotterynumbers):
    import random
lotteryNumbers = []
for i in range(0,7):
  number = random.randint(1,40)
  while number in lotteryNumbers:
    number = random.randint(1,40)
  lotteryNumbers.append(number)
lotteryNumbers.sort()

return lotteryNumbers