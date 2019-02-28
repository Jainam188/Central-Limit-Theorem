import pandas as pd
import random
import matplotlib.pyplot as plt

flights = pd.read_csv("Airlines.csv")

x1 = list(flights[flights['name'] == 'United Air Lines Inc.']['arr_delay'])
x2 = list(flights[flights['name'] == 'JetBlue Airways']['arr_delay'])
x3 = list(flights[flights['name'] == 'ExpressJet Airlines Inc.']['arr_delay'])
x4 = list(flights[flights['name'] == 'Delta Air Lines Inc.']['arr_delay'])
x5 = list(flights[flights['name'] == 'American Airlines Inc.']['arr_delay'])

# Assign colors for each airline and the names
colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73', '#D55E00']
names = ['United Air Lines Inc.', 'JetBlue Airways', 'ExpressJet Airlines Inc.',
         'Delta Air Lines Inc.', 'American Airlines Inc.']

col_a = list(x1)
col_b = list(x2)
col_c = list(x3)
col_d = list(x4)
col_e = list(x5)

i = 0


for i in range(0, 20):

    while i < 1000:
        i = i + 1

    sample1 = random.sample(col_a, i)
    sample2 = random.sample(col_b, i)
    sample3 = random.sample(col_c, i)
    sample4 = random.sample(col_d, i)
    sample5 = random.sample(col_e, i)

    plt.hist([sample1, sample2, sample3, sample4, sample5], color=colors, edgecolor='black', bins=int(180/15), label=names)
    plt.legend()
    plt.show()
