import random
import sys

agents = sys.argv[1:]

if  len(agents) < 2:
  exit("Provie at least two names as an input")

used = []

for agent in agents:
  options = [a for a in agents if a not in used and a is not agent]
  choice = random.choice(options) if len(options) > 2 or agents[-1] not in options else agents[-1]
  used.append(choice)

  print("{0} gives the presnet to {1}".format(agent,choice))




