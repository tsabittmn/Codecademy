# imports
import pandas as pd

# clas definitions
class MealPlan:
    """A class that keep all meals (breakfast, lunch,  & dinner)
    and their foods."""

    def __init__(self, meal_list):
        """
        Initialize the MealPlan instance.

        :param meal_list: A list consists of Meal objects.
        """
        self.meal_list = meal_list
        self.total_calories = 0
        self.total_proteins = 0
        self.total_carbs = 0
        self.total_fats = 0
        self.reach_target = False
    
    def update_macros(self):
        pass

    def show_result(self):
        pass

    def update_target(self):
        pass

class Meal:
    """A class that represent particular meal in the meal
    plan, and keep foods in it."""
    
    def __init__(self, food_list):
        """
        Initialize the Meal instance.

        :param food_list: A list consists of Food objects.
        """
        self.food_list = food_list
        self.total_calories = 0
        self.total_proteins = 0
        self.total_carbs = 0
        self.total_fats = 0
    
    def update_macros(self):
        pass

    def giveResult(self):
        pass
    
class Food:
    """A class that represent particular food in the meal, 
    and keep amount, categories, and macros in it."""

    def __init__(self, name, categories, macrosDataset):
        """
        Initialize the Food instance.

        :param food_list: A list consists of Food objects.
        """
        self.name = name
        self.categories = categories
        self.amount = 0
        # self.macros_dict = macros_dict


# function definitions
def loadDatasets():
    """
    Load the required datasets to run the program.

    Upon calling, this function will returns 3 datasets needed to 
    develop the meal plan.

    Returns:
        DataFrame: macros.csv
        DataFrame: caloriePerAct.csv
        DataFrame: macrosPerGoal.csv
    """
    macros = pd.read_csv('Codecademy/macros.csv')
    caloriePerAct = pd.read_csv('Codecademy/caloriePerAct.csv', index_col=0)
    macrosPerGoal = pd.read_csv('Codecademy/macrosPerGoal.csv', index_col=0)

    return macros, caloriePerAct, macrosPerGoal

def getUserInfo():
    """
    Prompt user to provide information needed.

    Upon calling, this function will call other helper functions
    to prompt user to provide information needed to develop the 
    meal plan.

    Returns:
        int: User’s weight
        str: User’s goal
        str: User’s activity level
    """
    weight = promptWeight()
    fitGoal = promptGoal()
    actLevel = promptAct()

    # check if actLevel is sedentary and fitGoal is leanGaining
    while actLevel == 'sedentary' and fitGoal == 'leanGaining':
        print("You shouldn't be lean gaining!")
        fitGoal = promptGoal()
    
    return weight, fitGoal, actLevel

def promptWeight():
     """
     Prompt user for weight in kg.

     This function prompts user for bodyweight in kilograms
     and return user's bodyweight in pounds.

     Returns:
        float: User's weight in pounds
     """
     answer = input("What is your weight(kg)?\n"
                    "Answer: ")
     
     return float(answer)*2.20462

def promptAct():
     """
     Prompt user for activity level.

     This function prompts user for activity level and return 
     string representation of that activity level.

     Returns:
        str: Activity level
     """
     answer = input("Please choose your current activity level:\n"
                    "'a': little or no exercise\n"
                    "'b': 1-4 hours of exercise per week\n"
                    "'c': 5-8 hours of exercise per week\n"
                    "'d': 9 or more hours of exercise per week\n"
                    "Answer: ")
     if answer == 'a':
          return 'sedentary'
     elif answer == 'b':
          return 'light'
     elif answer == 'c':
          return 'moderate'
     else:
          return 'high'
     
def promptGoal():
     """
     Prompt user for fitness goal.

     This function prompts user for current fitness goal to calculate 
     the target macros and returns the string representation of that 
     goal.

     Returns:
        str: Fitness goal
     """
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

def calcMacros(weight, actLevel, fitGoal, caloriePerAct, macrosPerGoal):
    """
    Calculate user's target macros.

    This function calculates user's target macros based on 
    weight, activity level, and fitness goal.

    Args:
        weight (float): User's weight
        actLevel (str): User's activity level
        fitLevel (str): User's fitness goal
        caloriePerAct (DataFrame): The caloriePerAct dataset
        macrosPerGoal (DataFrame): The macrosPerGoal dataset

    Returns:
        DataFrame: User's target macros
    """
    targetCal = round(weight * caloriePerAct.loc[actLevel, fitGoal])
    targetMacros = weight * macrosPerGoal.loc[fitGoal]
    targetMacros['calories'] = targetCal

    return targetMacros

def getMenu(macros, targetMacros):
    """
    Prompt user to choose treats and foods.

    Upon calling, this function will call other helper functions
    to prompt user to choose treats and foods to be added to the 
    meal plan.

    Args:
        macros (DataFrame): The macros dataset.
        targetMacros (DataFrame): User's targe macros.

    Returns:
        list: Treats choice
        dict: Food choices
    """
    treatChoice = promptTreat(macros, targetMacros)
    foodChoice = promptFood(macros)

    return treatChoice, foodChoice

def promptTreat(macros, targetMacros):
    """
    Prompt user for treats to add.

    This function prompts user for treats to add into the 
    meal plan. User's choice can't exceed 20% of target calories.
    This function returns list of treats chosen.

    Args:
        macros (DataFrame): The macros dataset.
        targetMacros (DataFrame): User's target macros.

    Returns:
        list: Chosen treats
    """
    # save treats options
    treatChoice = []
    maxCalories = targetMacros['calories'].item()*0.2

    # keep asking user to choose until done
    while True:
          print("Choose treats to add to your daily meals:")
          for treat in macros[macros['categories']=='treat']['food']:
               print("- " + treat) 
          print('- (done)')
          choice = input("Answer: ")
          if choice in treatChoice:
               print("That treats already added to your meals!")
          elif choice == 'done':
               break
          elif choice not in macros[macros['categories']=='treat']['food'].values:
               print("Treats not found! Please type the correct treats!")
          elif choice in macros[macros['categories']=='treat']['food'].values:
               calChoice = macros.loc[macros['food'] == choice, 'calories'].item()
               if maxCalories >= calChoice and choice not in treatChoice:
                    treatChoice.append(choice)
                    maxCalories -= calChoice
                    print(choice, "added to your treats!")
               elif maxCalories <= calChoice:
                    print('Chosen treats calories: ', calChoice)
                    print("Max calories: ", maxCalories)
                    print("Exceed maximum calories for treats!")

    return treatChoice

def promptFood(macros):
    """
    Prompt user for foods to add.

    This function prompts user for foods to add into the
    meal plan, which consists of breakfast, lunch, and dinner. 
    This function returns dictionary with meals as keys and 
    list of foods as the values.

    Args:
        macros (DataFrame): The macros dataset.

    Returns:
    dict: Foods for each meal
    """

    # final result
    foodChoice = {'breakfast':[], 'lunch':[], 'dinner':[]}

    # food options
    options = list(macros['food'])

    # iterate foodChoice
    for meal in foodChoice:
        done = False
        while done == False:
            print(f'Please select what you would like to add to your {meal}.')
           
            # show options
            for food in options:
                print('-', food)
            # input
            print(f"Type 'done' if you have finished selecting your {meal} items.")
            choice = input('Answer: ')

            # check if exist in data
            if choice in options:
                foodChoice[meal].append(choice)
            elif choice == 'done':
                done = True
            else:
                print("That food doesn't exist in macros.csv data!")   
    
    return foodChoice

def createMealPlan(targetMacros, treatChoice, foodChoice):
    pass

# main execution code
if __name__ == '__main__':
    macros, caloriePerAct, macrosPerGoal = loadDatasets()
    weight, fitGoal, actLevel = getUserInfo()
    targetMacros = calcMacros(weight, actLevel, fitGoal, caloriePerAct, macrosPerGoal)
    treatChoice, foodChoice = getMenu(macros, targetMacros)