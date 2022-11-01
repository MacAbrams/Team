import math

def mangos_per_day():
  print("=== How many mangos do you want to eat each day? ===")
  mangos = int(input("How many mangos? "))     
  days = int(input("How many days? "))
  result = mangos / days
  print(f"In order to eat {mangos} mangos in {days} days,")
  print(f"you'll need to eat {result} mangos per day.")

def main():
  print("Aloha!")
  mangos_per_day() 
