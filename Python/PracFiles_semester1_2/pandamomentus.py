# Importing pandas library
import pandas as pd

# Creating and initializing a nested list
age = [['Nimish', 95.5, "Male"], ['Shreyy', 65.7, "Male"],
	['Khushi', 85.1, "Female"], ['Krish', 75.4, "Male"]]

# Creating a pandas dataframe
df = pd.DataFrame(age, columns=['Name', 'Marks', 'Gender'])

# Printing dataframe
df
