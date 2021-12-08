import random

mode= input("Select difficulty. Easy Medium Hard: ")

while True:
  if (mode!="Easy" and mode!="Medium" and mode!="Hard"):
    print("This is not a correct level. ")
    mode= input("Select difficulty. Easy Medium Hard: ")
  else:
    break


if mode == ("Easy"):
  guess= int(input("Guess what number I am thinking of right now: "))
  numberEasy= random.randint(0, 10)
  while True:
    if guess != numberEasy:
      print("wrong")
      guess= int(input("Guess what number I am thinking of right now: "))
    else:
      print("right")
      break

elif mode == ("Medium"):
  guess= int(input("Guess what number I am thinking of right now: "))
  numberMedium= random.randint(0, 100)
  while True:
    if guess != numberMedium:
      print("wrong")
      guess= int(input("Guess what number I am thinking of right now: "))
    else:
      print("right")
      break

elif mode == ("Hard"):
  guess= int(input("Guess what number I am thinking of right now: "))
  numberHard= random.randint(0, 1000)
  while True:
    if guess < numberHard:
      print("wrong, too low")
      guess= int(input("Guess what number I am thinking of right now: "))
    elif guess > numberHard:
      print("Wrong, too high")
      guess= int(input("Guess what number I am thinking of right now: "))
    else:
      print("right")
      break
