# import necessary modules
import pandas as pd

# create the calPerAct dataset
c = {'activities': ['sedentary', 'lightAct', 'moderateAct', 'highAct'], 
     'cutting': [8, 10, 12, 14],
     'leanGaining': [14, 16, 18, 20],
     'maintaining': [12, 14, 16, 18]}
df = pd.DataFrame(data=c)
print(df)
