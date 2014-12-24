import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/chitown_crime_monthly.csv')

df['Date'] = pd.to_datetime(df['Date'])

# Make a new column just the year Interger of the year
df['Year'] = df['Date'].map(lambda x: x.year)

df['Month'] = df['Date'].map(lambda x: x.month)
# (If you wanted to make it the name of the Month)  # df['Month'] = df['Date'].map(lambda x: x.strftime('%B'))

# Lets just check out only the Arsons
arson = df[df['Primary Type'] == 'ARSON']

# Make a piviot table so the rows are the years, and the cols are the months, and the values are the countss
arson_pivot = arson.pivot('Year', 'Month', 'Count')
arson_pivot.head()


sns.heatmap(arson_pivot, annot=True);
plt.show()

# That is pretty good, but lets change some color and fix those y axis labels.
# use cmap to change color.
sns.heatmap(arson_pivot, annot=True, cmap='Spectral');

# Because seaborn is built ontop of Matplotlib. You can also refer to your seaborn chart with matplot commands
plt.yticks(rotation=0);

# Lets also make it bigger
plt.figure(figsize=(13,13));

plt.show()