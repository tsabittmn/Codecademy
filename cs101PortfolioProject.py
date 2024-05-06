# import necessary modules
import pandas as pd

# create the calPerAct dataset
c = {'activities': ['sedentary', 'lightAct', 'moderateAct', 'highAct'], 
     'cutting': [8, 10, 12, 14],
     'leanGaining': [14, 16, 18, 20],
     'maintaining': [12, 14, 16, 18]}
calPerAct = pd.DataFrame(data=c)

# loading macros data
location = "Codecademy/macros.csv"
macros = pd.read_csv(location)

# prompt user data
weight = input("What is your weight(kg)?\n"
               "Answer: ")
actLevel = input("Please choose your current activity level:\n"
                 "'a': little or no exercise\n"
                 "'b': 1-4 hours of exercise per week\n"
                 "'c': 5-8 hours of exercise per week\n"
                 "'d': 9 or more hours of exercise per week\n"
                 "Answer: ")
fitGoal = input("Please choose your body composition goal:\n"
                 "'a': cutting\n"
                 "'b': lean gaining\n"
                 "'c': maintaining\n"
                 "Answer: ")
treats = input("Choose treats to add:\n"
               "'a': dark chocolate\n"
               "'b': crackers & cheese\n"
               "'c': None\n"
               "Answer: ")







