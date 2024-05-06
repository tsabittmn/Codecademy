# import necessary modules
import pandas as pd

def loadData():
     """description"""

     # load calPerAct data
     c = {'activities': ['sedentary', 'lightAct', 'moderateAct', 'highAct'], 
          'cutting': [8, 10, 12, 14],
          'leanGaining': [14, 16, 18, 20],
          'maintaining': [12, 14, 16, 18]}

     # load macros data
     location = "Codecademy/macros.csv"
     macros = pd.read_csv(location)

     return pd.DataFrame(data=c), macros

def promptWeight():
     """description"""
     answer = input("What is your weight(kg)?\n"
                    "Answer: ")
     return answer

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
     elif answer == 'd':
          return 'highAct'
     else:
          print("That option is not exist!")
          return promptAct()
     
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
     return weight, actLevel, fitGoal         
     
def calcMacros():
     """description"""
    
# run the code
calPerAct, macros = loadData()
weight, actLevel, fitGoal = promptUser()







