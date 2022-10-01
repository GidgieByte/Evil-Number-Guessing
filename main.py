#Do you want to play a game of evil number guessing?
import os, random, sys

print("I'm thinking of a number between 1 and 100")

minNum = 1
maxNum = 100

for i in range(7): #Seven tries
  middleNum = int((maxNum - minNum) / 2) + minNum
  guess = int(input("Take a guess\n"))
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

print("Haha! You fool! The correct answer is " + str(answer) + "!")
