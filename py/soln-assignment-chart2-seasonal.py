import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Step 1:  Read data in. 
df = pd.read_csv('../data/chitown_crime_monthly.csv')

# Step 2:  Convert the Date column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# STEP 3: Make a column that is just the year interger ie 2012 YYYY 
df['YearInt'] = df['Date'].map(lambda x: x.year)

# STEP 4: Make a column that is just the number of the month
df['MonthInt'] = df['Date'].map(lambda x: x.month)

# STEP 5: Make a column that is just the number of the month
df['MonthName'] = df['Date'].map(lambda x: x.strftime('%b'))

# STEP 6: Groupby that month column you made, and sum the counts
df2 = df.groupby('MonthInt')['Count'].sum()

# STEP 8:  Plot the graph as you see fit.  
df2.plot()
plt.show()

# VARIATION TWO
df3 = df.groupby('YearInt')['Count'].sum()
df3.plot()
plt.show()

# VARIATION THREE

df3 = df.groupby(['Primary Type', 'YearInt'])['Count'].sum()
df3.unstack().T.plot()
plt.show()



