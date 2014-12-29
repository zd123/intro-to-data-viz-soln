
# coding: utf-8

# In[292]:

import pandas as pd
import matplotlib.pyplot as plt


# In[293]:

df = pd.read_csv('../data/50year-national-crime-population-totals.csv')
df.tail()


# In[294]:

### Chart 2:  Plotting population over time.  

# The first argument is your X-Axis, and second is Y-Axis, I chose to change the linewidth to 4 with lw=4
plt.plot(df['Year'], df['Population'], lw=4)

# Set the lower and upper bounds of the y axis
plt.ylim(0, 400000000.0 )

# Same for the x-axis, I just did what looked best to me
plt.xlim(1959,2013)

# Assign the title
plt.title('US National Population from 1960-2012')

# Assign the xlabel
plt.xlabel('Year')

# Assign the ylabel
plt.ylabel('Population in Hundred Millions')

# Create a grid, because I think grids are helpful for th eeye.  
plt.grid()


# In[295]:

# Chart 2: Bar Chart
plt.bar(df['Year'], df['Population'], width=1, alpha=0.75)
plt.ylim(0, 400000000.0 )
plt.xlim(1960, 2012)
plt.title('US National Population from 1960-2012')
plt.xlabel('Year')
plt.ylabel('Population in Hundred Millions')
plt.grid()


# In[295]:




# In[296]:

# Chart 3: Plotting total crime and population.
df = pd.read_csv('../data/50year-national-crime-population-totals.csv')
df = df.set_index(df['Year'])
df[['Population', 'total_crime']].plot(secondary_y=['total_crime'])


# In[297]:

# Chart 3: Plotting total crime and population.
# The really annoying way to do it, without using pandas. 

# Create just one subplot 
fig, ax = plt.subplots()

ax.plot(df['Year'], df['Population'], lw=2, c='b',label='Population')

# This will return to you the location of each of the yticks
tick_locs = ax.get_yticks()

# What we want to do is turn that into something human readable. 
tick_text = [ x / 1000000.0 for x in tick_locs ]

# Then, set_yticklabels with our new formated tick_text
ax.set_yticklabels(tick_text, color='b')

# Set the location of the legend so the next one doesn't fall ontop of it
ax.legend(loc='upper left')


# Since we want to plot them both on the same plot, we duplicate the first ax
ax2 = ax.twinx()

# Plot our other data on our duplicated axis
ax2.plot(df['Year'], df['total_crime'], lw=2, c='r', label='Crime')

# Again, get the tick locations
tick_locs = ax2.get_yticks()

# Reformat that number to the number we want
tick_text = [ x / 1000000.0 for x in tick_locs ]

# Place our new tick-text labels
ax2.set_yticklabels(tick_text, color='r')

# Place our legend in the lower right. 
ax2.legend(loc='lower right')

ax.set_xlim(1959, 2012)


# In[319]:

# Chart 4: Which year had the highest rate of crime...
df = pd.read_csv('../data/50year-national-crime-population-totals.csv')

df['crime_rate'] = df['total_crime'] / df['Population']
plt.bar(df['Year'], df['crime_rate'], width=1, alpha=0.75);
plt.grid()
plt.xlim(1959,2014)
plt.title('Crime rate in the U.S.')
plt.ylabel('Amount of Crime')
plt.xlabel('Year')


# In[379]:

### Chart 5: Plot all the trends of crimes using subplots.

# Create a subplot with 2 rows and 4 columns
fig, ax = plt.subplots(nrows=2, ncols=4, figsize=(21,13))

nrows = 2
ncols = 4
counter = 0

# List of charts to plot
cols_to_plot = [ u'Murder and nonnegligent Manslaughter', u'Forcible rape', u'Robbery', u'Aggravated assault', u'Property crime total', u'Burglary', u'Larceny-theft', u'Motor vehicle theft']

# Loop through nrows and ncols
for r in range(nrows):
    for c in range(ncols):
        # first pass will be ax[0,0] that is our first plot, 
        ax[r,c].plot( df['Year'], df[cols_to_plot[counter]] )

        # Use the counter to access the list that has our column names
        ax[r,c].set_title( cols_to_plot[counter] ) 
        
        # Set whatever params you would like here
        ax[r,c].set_xlim(1959,2013)
        
        #Update your counter 
        counter += 1 


# In[ ]:



