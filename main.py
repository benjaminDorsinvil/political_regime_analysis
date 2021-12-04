import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('political-regimes.csv')

# Investigating
print(data.describe())
print(data.info())

# Finding null in the dataset
print(data.isnull().sum())

# finding all the null columns
print(data[data.isnull().any(axis=1)].head())

# finding the unique null values
print(data[data.isnull().any(axis=1)]['Entity'].unique())

# Fixing the null
item_dict = {
    'Brunswick': 'NKC',
    'German Democratic Republic': 'DDR',
    'Hesse-Darmstadt': 'HES',
    'Oldenburg': 'OLD',
    'Palestine/Gaza': 'PSE',
    'Palestine/West Bank': 'PSE',
    'Papal States': 'VAT',
    'Piedmont-Sardinia': 'ITA',
    'Saxe-Weimar-Eisenach': 'SXM',
    'South Yemen': 'YEM',
    'Wuerttemberg': 'WUE'
}


def item_mappnig(df, dictionary, colsource, coltarget):
    dict_keys = list(dictionary.keys())
    dict_values = list(dictionary.values())
    for x in range(len(dict_keys)):
        df.loc[df[colsource] == dict_keys[x], coltarget] = dict_values[x]
    return df


item_mappnig(data, item_dict, 'Entity', 'Code')

# replacing the numbers in political regime column
political_dict = {
    0: 'Closed Autocracies',
    1: 'Electoral Autocracies',
    2: 'Electoral Democracies',
    3: 'Liberal Democracies'
}

item_mappnig(data, political_dict, 'Political regime', 'Political regime')

# Political Regime graph
most_recent = data[data['Year']>=2005]

p= sns.catplot(x='Political regime', hue='Year', data=most_recent, kind='count', palette='flare')
sns.set(rc = {'figure.figsize':(15,10)})
plt.title('Political Regimes over The Last 5 Years', fontweight="bold")
plt.xlabel('Political Regimes', fontweight="bold")
plt.ylabel('Count', fontweight="bold")
plt.xticks(rotation=45)
plt.show()

# count of electoral and liberal democracies
elect_demo = data[data['Political regime'] == 'Electoral Democracies']['Entity'].count()
lib_demo = data[data['Political regime'] == 'Liberal Democracies']['Entity'].count()
print('The number of countries with electoral democracies is: {}'.format(elect_demo))
print('The number of countries with liberal democracies is: {}'.format(lib_demo))

# graph the counts
ax = sns.countplot(x='Political regime', data=data, palette="deep")
for container in ax.containers:
    ax.bar_label(container)

sns.set(rc = {'figure.figsize':(16,10)})
plt.title('Total Political Regimes', fontweight="bold")
plt.xlabel('Political Regimes', fontweight="bold")
plt.ylabel('Total', fontweight="bold")
plt.xticks(rotation=45)
plt.show()

