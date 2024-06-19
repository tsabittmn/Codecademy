# import modules
import pandas as pd

# function definitions
def loadDatasets():
    """
    Load the required datasets to run the program.

    Upon calling, this function will returns 4 datasets needed to 
    develop the meal plan.

    Returns:
        DataFrame: macros.csv
        DataFrame: treats.csv
        DataFrame: caloriePerAct.csv
        DataFrame: macrosPerGoal.csv
    """
    macros = pd.read_csv('Codecademy/macros.csv')
    treats = pd.read_csv('Codecademy/treats.csv')
    caloriePerAct = pd.read_csv('Codecademy/caloriePerAct.csv')
    macrosPerGoal = pd.read_csv('Codecademy/macrosPerGoal.csv')

    return macros, treats, caloriePerAct, macrosPerGoal

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
        str: Treat choice
        dict: Food choices
    """
    

def addOwnTreat():
    """
    """

def addOwnFood():
    """
    """

#### TESTING ####
