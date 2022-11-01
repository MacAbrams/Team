import diceCalc
import menuLib
import woodchuck as wc
import run

#add your functions here
options = [
  diceCalc.calc_prob_dice_num, diceCalc.calc_prob_dice_sides,
  diceCalc.calc_prob_dice_num_w_sides, diceCalc.rollOffTies, diceCalc.rollDice,
  run.yeargoaltomonth, run.minutemilepace, run.kilometersamile,
  run.milesperkilometer,
  wc.woodChuckBrain.wood_per_chuck,wc.woodChuckBrain.chuck_speed , wc.woodChuckBrain.strength_of_chucks,
  wc.woodChuckBrain.wood_per_second
]


desc = [
  "odds of n dice where the highest is above a number",
  "odds of a n sided dice rolling above a number", "odds many dice and sides",
  "odds of rolloffs with many dice", "roll some dice",
  "Yearly, Monthly, Weekly, and Daily Mileage", "Minute per Mile of your Run",
  "Mile Distance to Kilometer Distance", "Kilometer Distance to Mile Distance", "Wood per Chuck", "Chuck speed", "Strength of chucks", "Wood per second"
]


def main():
  # menu2 = menuLib.Menu()
  menu = menuLib.Menu("Welcome to Wood Calculator", options, desc)
  # menu.add(menu2.menu)
  # print(menu2.menu)
  # diceCalc.selector()
  # run.selector()
  menu.menu()


main()
