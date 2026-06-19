import pandas as pd
import numpy as np
bios = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\data\bios.csv")
coffee = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\warmup-data\coffee.csv")
print(bios['born_city'].value_counts())
#this line counts how many times each unique city appears in the born_city column.
"""
born_city
Budapest            1378
Moskva (Moscow)      883
Oslo                 708
Stockholm            629
Praha (Prague)       600
                    ... 
Tsivilsk               1
Roth                   1
Romoos                 1
Dva Polya Artash       1
Dulwich Hill           1
"""
print(bios[bios['born_country']=='USA']['born_region'].value_counts().head())
# Find all athletes who were born in the USA, then count how many athletes are from each region/state
"""
# Select athletes whose born_country is USA,
# then select their born_region (state/region),
# count how many times each region appears,
# and print the regions sorted from highest to lowest count.

print(bios[bios['born_country'] == 'USA']['born_region'].value_counts())
"""
"""
born_region
California       1634
New York          990
Illinois          585
Pennsylvania      530
Massachusetts     530
"""
print(coffee.groupby(['Coffee Type'])['Units Sold'].sum())
"""
Coffee Type
Espresso    265
Latte       195
"""
coffee['price']=5.9
print(coffee.head())
print(coffee.groupby(['Coffee Type']).agg({'Units Sold': 'sum','price':'mean'}))
"""
             Units Sold  price
Coffee Type                   
Espresso            265    5.9
Latte               195    5.9
"""
print(coffee.groupby(['Coffee Type','Day']).agg({'Units Sold': 'sum','price':'mean'}))
"""
                       Units Sold  price
Coffee Type Day                         
Espresso    Friday             45    5.9
            Monday             25    5.9
            Saturday           45    5.9
            Sunday             45    5.9
            Thursday           40    5.9
            Tuesday            30    5.9
            Wednesday          35    5.9
Latte       Friday             35    5.9
            Monday             15    5.9
            Saturday           35    5.9
            Sunday             35    5.9
            Thursday           30    5.9
            Tuesday            20    5.9
            Wednesday          25    5.9
"""
coffee['revenue'] = coffee['Units Sold'] * coffee['price']
pivot = coffee.pivot(columns = 'Coffee Type' , index = 'Day' , values = 'revenue')
print(pivot)
# .pivot() is used to reshape a DataFrame by converting unique values from one column into new columns and organizing data in a table format.
"""
Coffee Type  Espresso  Latte
Day                         
Friday          265.5  206.5
Monday          147.5   88.5
Saturday        265.5  206.5
Sunday          265.5  206.5
Thursday        236.0  177.0
Tuesday         177.0  118.0
Wednesday       206.5  147.5
"""
bios['born_date'] = pd.to_datetime(bios['born_date'])
print(bios.groupby(bios['born_date'].dt.year)['name'].count().head())
"""
born_date
1828.0    1
1831.0    2
1833.0    1
1836.0    1
1837.0    1
"""
print(bios.groupby(bios['born_date'].dt.year)['name'].count().reset_index().sort_values('name',ascending=False).head())
"""
     born_date  name
139     1972.0  2231
152     1985.0  2227
140     1973.0  2216
138     1971.0  2205
137     1970.0  2174
"""
bios['month_born'] = bios['born_date'].dt.month
bios['year_born'] = bios['born_date'].dt.year
print(bios.groupby([bios['year_born'],bios['month_born']])['name'].count().reset_index().sort_values('name' , ascending = False))
"""
      year_born  month_born  name
1437     1970.0         1.0   239
1461     1972.0         1.0   229
1497     1975.0         1.0   227
1629     1986.0         1.0   227
1617     1985.0         1.0   225
...         ...         ...   ...
1877     2006.0        12.0     1
1871     2006.0         3.0     1
20       1846.0         7.0     1
21       1846.0         8.0     1
22       1846.0         9.0     1
"""
coffee['yesterday_revenue'] = coffee['revenue'].shift(1)
print(coffee.head())
"""
         Day Coffee Type  Units Sold  price  revenue  yesterday_revenue
0     Monday    Espresso          25    5.9    147.5                NaN
1     Monday       Latte          15    5.9     88.5              147.5
2    Tuesday    Espresso          30    5.9    177.0               88.5
3    Tuesday       Latte          20    5.9    118.0              177.0
4  Wednesday    Espresso          35    5.9    206.5              118.0
"""