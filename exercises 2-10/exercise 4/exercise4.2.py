import random
x = int(input("How many sets of lottery numbers to generate: "))

def lottery(x):
  for x in range(x):
    lotnum = random.sample(range(1,41),7)
    lotnum = sorted(lotnum)
    print(*lotnum, sep=",")

lottery(x)