# import necessary modules
import pandas as pd

def loadData():
     """load datasets that are needed for the program to run"""

     # load calPerAct data
     calPerAct = pd.DataFrame( 
          {'cutting': [8, 10, 12, 14],
          'leanGaining': [14, 16, 18, 20],
          'maintaining': [12, 14, 16, 18]},
          index = ['sedentary', 'lightAct', 'moderateAct', 'highAct'])
     
     # load macPerGoal data
     macPerGoal = pd.DataFrame(
          {'protein': [1.2, 1.0, 1.0],
          'carbs': [2.0, 2.0, 2.0],
          'fat': [0.4, 0.4, 0.4]},
          index = ['cutting', 'leanGaining', 'maintaining'])

     # load macros data
     location = "Codecademy/macros.csv"
     macros = pd.read_csv(location)

     # load treats data
     location = "Codecademy/treats.csv"
     treats = pd.read_csv(location)

     return calPerAct, macPerGoal, macros, treats

def promptWeight():
     """description"""
     answer = input("What is your weight(kg)?\n"
                    "Answer: ")
     
     return float(answer)*2.20462

def promptAct():
     """description"""
     answer = input("Please choose your current activity level:\n"
                    "'a': little or no exercise\n"
                    "'b': 1-4 hours of exercise per week\n"
                    "'c': 5-8 hours of exercise per week\n"
                    "'d': 9 or more hours of exercise per week\n"
                    "Answer: ")
     if answer == 'a':
          return 'sedentary'
     elif answer == 'b':
          return 'lightAct'
     elif answer == 'c':
          return 'moderateAct'
     else:
          return 'highAct'
     
def promptGoal():
     """description"""
     answer = input("Please choose your body composition goal:\n"
                    "'a': cutting\n"
                    "'b': lean gaining\n"
                    "'c': maintaining\n"
                    "Answer: ")
     if answer == 'a':
          return 'cutting'
     elif answer == 'b':
          return 'leanGaining'
     elif answer == 'c':
          return 'maintaining'
     else:
          print("That option is not exist!")
          return promptGoal()
     
def promptUser():
     """description"""
     weight = promptWeight()
     actLevel = promptAct()
     fitGoal = promptGoal()
     
     # check if actLevel is sedentary and fitGoal is leanGaining
     while actLevel == 'sedentary' and fitGoal == 'leanGaining':
          print("You shouldn't be lean gaining!")
          fitGoal = promptGoal()
     
     return weight, actLevel, fitGoal         
     
def calcMacros(weight, actLevel, fitGoal):
     """
     calculate user's target macros
     given weight, activity level, and fitness
     goal
     """
     targetCal = round(weight * calPerAct.loc[actLevel, fitGoal])
     targetMac = weight * macPerGoal.loc[fitGoal]
     targetMac['calories'] = targetCal

     return targetMac

def chooseTreats(targetCalories, treats):
     """
     Prompt user to choose treats to add to the menu
     from the 'treats' dataset.

     return: list of choosen treats.
     """

     # keep track of variables
     treatsList = []
     maxTreats = targetCalories*0.2

     # show treats options
     while True:
          print("Choose treats to add to your daily meals:")
          for treat in treats['food']:
               print("- " + treat) 
          choice = input("Answer: ")
          if choice in treatsList:
               print("That treats already added to your meals!")
          elif choice == 'done':
               break
          elif choice not in treats['food'].values:
               print("Treats not found! Please type the correct treats!")
          elif choice in treats['food'].values:
               calChoice = treats.loc[treats['food'] == choice, 'calories'].item()
               if maxTreats >= calChoice and\
                    choice not in treatsList:
                    treatsList.append(choice)
                    maxTreats -= calChoice
                    print(choice, "added to your treats!")
               elif maxTreats <= calChoice:
                    print('Chosen treats calories: ', calChoice)
                    print("Max calories: ", maxTreats)
                    print("Exceed maximum calories for treats!")
          
     # update target macros
       
     
     return treatsList 

# run the code
calPerAct, macPerGoal, macros, treats = loadData()
weight, actLevel, fitGoal = promptUser()
targetMac = calcMacros(weight, actLevel, fitGoal)

# tests
print(chooseTreats(targetMac['calories'], treats))