import os

import sys


class Menu:

  def default(self):
    sys.exit(0)
    return 0

  def __init__(self, name=None, opt=None, desc=None):
    self.options = []
    self.string = []
    if opt != None:
      if desc == None:
        for i in range(len(opt)):
          self.add(opt[i])
      else:
        for i in range(len(opt)):
          if i in range(len(desc)):
            self.add(opt[i], desc[i])
          else:
            self.add(opt[i])

    if name == None:
      self.title = "Menu"
    else:
      self.title = name
    self.repeat = True
    self.cursor = ">"
    self.default = self.default

  def setTitle(self, i_title):
    self.title = i_title
    return 0
  def addHeader(self):
    return 0
  def noRepeat(self):
    self.repeat = False
    return 0

  def setDefault(self, num):
    self.default = self.options[num]
    return 0

  def setCursor(self, i_curs):
    self.cursor = i_curs
    return 0

  def add(self, func, desc=None):
    temp = [None] * (len(self.options) + 1)
    for i in range(len(self.options)):
      temp[i] = self.options[i]
    temp[len(self.options)] = func
    self.options = temp
    temp = [None] * (len(self.string) + 1)
    for i in range(len(self.string)):
      temp[i] = self.string[i]
    self.string = temp
    if desc == None:
      desc = str(func)[10:]
      for i in range(len(desc)):
        if desc[i] == " ":
          desc = desc[:i]
          break
    self.string[len(self.string) -
                1] = "\n\t" + str(len(self.options)) + " => " + str(desc)
    return 0

  def menu(self):
    os.system("clear")
    print("+==" + "=" * len(self.title) + "+")
    print("| " + self.title + " |")
    print("+==" + "=" * len(self.title) + "+\n")
    s = ""
    for i in range(len(self.string)):
      s = s + self.string[i]
    print("Options:" + s)
    #add your option text here
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
      opt = input(self.cursor)
      if opt.lower() == "q":
        sys.exit(0)
      elif opt == "":
        self.default()
      elif opt.isdigit() and int(opt) - 1 in range(len(self.options)):
        print(self.options[int(opt) - 1]())
        acceptable = True
        if self.repeat:
          input("RET for menu")
        else:
          return 0
      else:
        print("Sorry please select an valid option")
      if not self.repeat:
        return 0

    self.menu()
