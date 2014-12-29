
# coding: utf-8

# In[194]:

import pandas as pd
import matplotlib.pylab as plt


# In[195]:

df = pd.read_csv('data/chitown_crime_arrests_vs_reports.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.head()


# In[196]:

# Create a bar chart that shows the amout of arrests made each month.
df['Arrests'].plot(kind='bar')


# In[197]:

# Take the columns MonthStr and Arrests out of the dataframe 
data = df['Arrests'].values
months = df['MonthStr'].values

# THIS IS HOW TO GET THE MONTH NAME FROM A DATETIME OBJECT 
# df['Date'].map(lambda x: x.strftime('%b')).values


# In[198]:

# Create a barplot with the height of the bar is the number of arrests for each month
plt.bar(left=range(len(data)), height=data)


# In[199]:

# Now customize your x-ticks to be the month names, and not just intergers
plt.bar(left=range(len(data)), height=data)
tick_locations = range(len(months))
plt.xticks(tick_locations, months);


# In[200]:

# Make the plot bigger, make it 13 x 8
plt.figure(figsize=(13,8))
plt.bar(left=range(len(data)), height=data)
tick_locations = range(len(months))
plt.xticks(tick_locations, months);




# In[201]:

# Make the Y-axis height to range from 0 to 10000 instead of 9000
plt.figure(figsize=(13,8))
plt.bar(left=range(len(data)), height=data)
tick_locations = range(len(months))
plt.xticks(tick_locations, months);
plt.ylim(0,10000);


# In[202]:

# Align the xlabels to be in the center of each bar
plt.figure(figsize=(13,8))
plt.bar(left=range(len(data)), height=data, align='center')
tick_locations = range(len(months))
plt.xticks(tick_locations, months)
plt.ylim(0,10000);


# In[203]:

# If that alignment make your graph look a bit wonky, try adjusting the xlim to fix it

plt.figure(figsize=(13,8))
plt.bar(left=range(len(data)), height=data, align='center')
plt.grid(True, c='0.25')

tick_locations = range(len(months))
plt.xticks(tick_locations, months)
plt.ylim(0,10000)
plt.xlim(-1,12);

