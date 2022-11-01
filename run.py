import math


#yearstoday
def yeargoaltomonth():
  print("=== New Year: Yearly, Monthly, Weekly, Daily mileage ===")
  print()
  yeartotal = int(input("How many miles in a year(full number value)? "))
  result = yeartotal / 12
  result2 = yeartotal / 52
  day = int(input("How many days are left in the week? "))
  result3 = (result2 / day)
  result4 = (result2 / 7)
  print(f"If you want to run {yeartotal} miles a year,")
  print(f"then you need to run {result} miles a month,")
  print(f"{result2} miles a week")
  print(f"{result4} average per day on a typical week")
  print(f"or {result3} miles, on average, a day for this week.")


#minutemilepace
def minutemilepace():
  print("=== Minutes per mile ===")
  time = int(
    input(
      "How many minutes did you run if round to the nearest full minute? "))
  length = int(
    input(
      "How many miles did you run, round it to the nearest full number --> "))
  result = (time / length)
  print(f"If you want to run for {time} minutes, and run {length} miles,")
  print(f"then your minute per mile is {result} minutes.")


#kilometerstomiles
def kilometersamile():
  print("=== Kilometers Run per Miles Run ===")
  miles = int(
    input("How many miles did you run(round to closest full number)? "))
  result = miles * 1.6
  print(f"If you ran for {miles} miles,")
  print(f"then you ran {result} kilometers.")


#milestokilometers
def milesperkilometer():
  print("=== Miles Run per Kilometers Run ===")
  kilometers = int(
    input("How many kilometers did you run(round to closest full number)? "))
  result = kilometers * 0.62137
  print(f"If you ran for {kilometers} kilometers,")
  print(f"then you ran {result} miles.")


def showmenu():
  print("")
  print("Welcome the runner's calculator!")
  print("Your helper in determining any of your running needs!")
  print()
  print("The available calculations are:")
  print("1 = Yearly, Monthly, Weekly, and Daily Mileage")
  print("2 = Minute per Mile of your Run")
  print("3 = Mile Distance to Kilometer Distance")
  print("4 = Kilometer Distance to Mile Distance")
  print()


def selector():
  showmenu()
  choice = (int(input("What Calculation do you need? ")))
  if choice == 1:
    yeargoaltomonth()
  elif choice == 2:
    minutemilepace()
  elif choice == 3:
    kilometersamile()
  elif choice == 4:
    milesperkilometer()
  else:
    print("not a valid option!")
