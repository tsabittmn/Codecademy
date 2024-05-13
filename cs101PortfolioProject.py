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
     macros = pd.read_csv(location, header=0, index_col=0)

     # load treats data
     location = "Codecademy/treats.csv"
     treats = pd.read_csv(location, header=0, index_col=0)

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

def chooseTreats(treats, targetMac):
     """
     Prompt user to choose treats to add to the menu
     from the 'treats' dataset.

     return: list of choosen treats.
     """

     # keep track of variables
     treatsList = []
     maxTreats = targetMac['calories']*0.2

     # show treats options
     while True:
          print("Choose treats to add to your daily meals:")
          for treat in treats['food']:
               print("- " + treat) 
          print('- (done)')
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
     # for each treat in treatsList
     for treat in treatsList:

          # for each macro in targetMac
          for mac in targetMac.index:

               # reduce macro by macro from treat
               targetMac[mac] -= treats.loc[treats['food'] == treat, mac].item()

     return treatsList, targetMac

def promptMenu():
     """
     Prompt user to choose which food for each meal.
     
     Return: dictionary with format {meal1:[food1, food2, food3], meal2:[], etc.}
     """
     foodChoice = {'breakfast':[], 'lunch':[], 'dinner':[]}
     
     # iterate foodChoice
     for meal in foodChoice:
          done = False
          while done == False:
               print(f'Please select what you would like to add to your {meal}.')
               # show options
               for food in macros.index:
                    print('-', food)
               # input
               print(f"Type 'done' if you have finished selecting your {meal} items.")
               choice = input('Answer: ')

               # check if exist in data
               if choice in macros.index:
                    foodChoice[meal].append(choice)
               elif choice == 'done':
                    done = True
               else:
                    print("That food doesn't exist in macros.csv data!")   
     
     return foodChoice

class Food:
     def __init__(self, name, amount):
          self.name = name
          self.amount = amount
          self.calories = macros.at[name, 'calories']*(amount/100)
          self.protein = macros.at[name, 'protein']*(amount/100)
          self.carbs = macros.at[name, 'carbs']*(amount/100)
          self.fat = macros.at[name, 'fat']*(amount/100)
          self.categories = macros.at[name, 'categories']
    
     def __repr__(self):
          return self.name + " " + str(self.amount) + " gr"
     
     def increaseAmount(self, name, amount):
          self.amount += 1
          self.calories = macros.at[name, 'calories']*(amount/100)
          self.protein = macros.at[name, 'protein']*(amount/100)
          self.carbs = macros.at[name, 'carbs']*(amount/100)
          self.fat = macros.at[name, 'fat']*(amount/100)

     def decreaseAmount(self, name, amount):
          self.amount -= 1
          self.calories = macros.at[name, 'calories']*(amount/100)
          self.protein = macros.at[name, 'protein']*(amount/100)
          self.carbs = macros.at[name, 'carbs']*(amount/100)
          self.fat = macros.at[name, 'fat']*(amount/100)

# run the code
calPerAct, macPerGoal, macros, treats = loadData()
# weight, actLevel, fitGoal = promptUser()
# targetMac = calcMacros(weight, actLevel, fitGoal)
# treatsList, targetMac = chooseTreats(treats, targetMac)
foodChoice = promptMenu()

# tests
# targetMac = calcMacros(65*2.20462, 'moderateAct', 'leanGaining')
