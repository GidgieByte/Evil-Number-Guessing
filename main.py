#Do you want to play a game of evil number guessing?
import os, random, sys
import pyinputplus as pyip

minNum = 1
maxNum = 100

print(f"I'm thinking of a number between {minNum} and {maxNum}")

for i in range(7, 0, -1): #Seven tries
  middleNum = int((maxNum - minNum) / 2) + minNum
  plur = "es"
  if i == 1:
    plur = ""
  guess = pyip.inputNum(prompt = f"You have {i} guess{plur} left\n", blockRegexes=[r'\.'])
  if minNum == maxNum and guess == minNum: #There are no more available numbers; the computer has nowhere else to go
    print("You have bested me!")
    #The player has won so the program ends. This command also throws the error 'repl process died unexpectedly:' which I find hilarious and refuse to change.
    sys.exit()
  elif guess > middleNum: #There are more available numbers that are less than the current guess
    print("too high")
    if guess <= maxNum:
      maxNum = guess - 1
  else: #There are more available numbers that are greater than the current guess 
    print("too low")
    if guess >= minNum: 
      minNum = guess + 1

#The player was unable to guess the right number; the computer picks a random number within the range that's still available 
answer = random.randint(minNum, maxNum)

print(f"Haha! You fool! The correct answer was {answer}!")
