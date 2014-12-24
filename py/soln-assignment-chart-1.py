import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# Load in the yearly data. 
df = pd.read_csv('../data/chitown_crime_yearly.csv')

# Convert the Date column to a datetime object.
df['Date'] = pd.to_datetime(df['Date'])

# Set the Date column to be the index.
df = df.set_index('Date')


# Because the index is a datetime object. 
# We can use the pandas resample function which is like a groupby for time.
# The 'A' means groupby year... if you did 'M' it would be month.
# The docs for df.resample() are here.  http://bit.ly/13F2XvP

# So we groupby the year and sum the counts of the crime, then plot them as a bar plot 
df.resample(rule='A', how='sum').plot(kind='bar')

# Now display the chart. This should pop up in your window
plt.show()


'''
TIME FREQUENCYS RULE CODES FOR PANDAS .resample(rule='M') FUNCTION
===============================================
B   business day frequency
C   custom business day frequency (experimental)
D   calendar day frequency
W   weekly frequency
M   month end frequency
BM  business month end frequency
MS  month start frequency
BMS business month start frequency
Q   quarter end frequency
BQ  business quarter endfrequency
QS  quarter start frequency
BQS business quarter start frequency
A   year end frequency
BA  business year end frequency
AS  year start frequency
BAS business year start frequency
H   hourly frequency
T   minutely frequency
S   secondly frequency
L   milliseconds
U   microseconds
'''




