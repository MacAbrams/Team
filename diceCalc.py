import math
import random
import os
import sys


def calc_prob_dice_num():
  dice = int(input("how many dice are you rolling? "))
  sideNum = 6
  num = int(input("What number do you need to roll above? "))
  ans = 1 - math.pow(1 - ((sideNum - num) / sideNum), dice)
  return str(ans * 100) + "% chance"


def calc_prob_dice_sides():
  diceSides = int(input("how many sides do the dice have? "))
  num = int(input("What number do you need to roll above? "))
  ans = ((diceSides - num) / diceSides)
  return str(ans * 100) + "% chance"


def calc_prob_dice_num_w_sides():
  dice = int(input("how many dice are you rolling? "))
  sideNum = int(input("how many sides do the dice have? "))
  num = int(input("What number do you need to roll above? "))
  ans = 1 - math.pow(1 - ((sideNum - num) / sideNum), dice)
  return str(ans * 100) + "% chance"


def rollOffTies():
  n = int(input("How many sides are on the dice? "))
  diceMe = int(input("How many dice are you rolling? "))
  diceOp = int(input("How many dice is your opponent rolling? "))
  probArrMe = {}
  probArrOp = {}
  for i in range(n):
    at = 1 - (math.pow(1 - (((n) - (i)) / n), diceMe))
    abv = 1 - (math.pow(1 - (((n) - (i + 1)) / n), diceMe))
    probArrMe[i] = at - abv
  for i in range(n):
    at = 1 - (math.pow(1 - (((n) - (i)) / n), diceOp))
    abv = 1 - (math.pow(1 - (((n) - (i + 1)) / n), diceOp))
    probArrOp[i] = at - abv
  ans = 0
  ties = 0
  for i in range(n):
    for j in range(n):
      if i > j:
        ans += probArrOp[j] * probArrMe[i]
      if i == j:
        ties += probArrOp[j] * probArrMe[i]

  #   1/4 1/4 1/4 1/4
  #1/4 n    y   y   y
  #1/4 n    n   y   y
  #1/4 n    n   n   y
  #1/4 n    n   n   n
  space = ""
  winNum = str(round(ans * 100, 5))
  if len(winNum) == 7:
    space = " "
  win = "Winning: " + space + winNum + "% chance\n"
  tieNum = str(round((ties * 100), 5))
  if len(tieNum) == 7:
    space = " "
  tie = "Ties:    " + space + tieNum + "% chance\n"
  loseNum = str(round((1 - (ans + ties)) * 100, 5))
  if len(loseNum) == 7:
    space = " "
  loses = "Losing:  " + space + loseNum + "% chance"
  return win + tie + loses


def diceRoller(sideNum, diceNum):
  size = os.get_terminal_size()
  coloumns = str(size)[25:]
  for i in range(len(coloumns)):
    if coloumns[i] == ",":
      coloumns = int(coloumns[:i])
      break
  out = ""
  top = "\t" * 2
  mid = "\t" * 2
  bot = "\t" * 2
  topper = "┌" + "─" * (len(str(sideNum))) + "┐"
  botter = "└" + "─" * (len(str(sideNum))) + "┘"
  total = 0
  for i in range(diceNum):
    if len((str(top) + "\t" + str(topper)).expandtabs()) >= coloumns:
      out += "\n" + top[1:] + "\n" + mid + "\n" + bot[1:]
      top = "\t" * 2
      mid = "\t" * 2
      bot = "\t" * 2
    t = random.randint(1, sideNum)
    total += t
    t = str(t)
    space = " " * (len(str(sideNum)) - len(t))
    top += "\t" + topper
    mid += "│" + space + str(t) + "│\t"
    bot += "\t" + botter
  out += "\n" + top[1:] + "\n" + mid + "\n" + bot[1:]

  # return top+"\n"+mid
  top = "───────" + "─" * len(str(total))
  return out + "\n┌" + top + "┐\n" + "│Total: " + str(
    total) + "│\n└" + top + "┘\n"


def rollDice():
  sideNum = int(input("How many sides? "))
  diceNum = int(input("How many dice? "))
  print(diceRoller(sideNum, diceNum))
  size = os.get_terminal_size()
  coloumns = str(size)[25:]
  for i in range(len(coloumns)):
    if coloumns[i] == ",":
      coloumns = int(coloumns[:i])
      break
  print("=" * coloumns)
  reroll = input("reroll? [Y/n]:")

  while True:
    if reroll.lower() == "y" or reroll == "":
      print(diceRoller(sideNum, diceNum))
      size = os.get_terminal_size()
      coloumns = str(size)[25:]
      for i in range(len(coloumns)):
        if coloumns[i] == ",":
          coloumns = int(coloumns[:i])
          break
      print("=" * coloumns)
      reroll = input("Reroll? [Y/n]: ")
    else:
      break
  return ""


options = [
  calc_prob_dice_num, calc_prob_dice_sides, calc_prob_dice_num_w_sides,
  rollOffTies, rollDice
]


def selector():
  os.system("clear")
  print("+==========================+")
  print("|Welcome to Dice Calculator|")
  print("+==========================+\n")

  print("Options:")
  print("\t1 => odds of n dice where the highest is above a number")
  print("\t2 => odds of a n sided dice rolling above a number")
  print("\t3 => odds many dice and sides")
  print("\t4 => odds of rolloffs with many dice")
  print("\t5 => roll some dice")
  print("\tQ => quit")
  size = os.get_terminal_size()
  coloumns = str(size)[25:]
  for i in range(len(coloumns)):
    if coloumns[i] == ",":
      coloumns = int(coloumns[:i])
      break
  print("=" * coloumns)
  acceptable = False
  while not acceptable:
    opt = input(">")
    if opt.lower() == "q":
      sys.exit(0)
    elif opt.isdigit() and int(opt) - 1 in range(len(options)):
      print(options[int(opt) - 1]())
      acceptable = True
      input("RET for menu")
    else:
      print("Sorry please select an valid option")
  selector()
