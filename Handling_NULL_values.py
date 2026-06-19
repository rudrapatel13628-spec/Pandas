import pandas as pd
import numpy as np
coffee = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\warmup-data\coffee.csv")
coffee.loc[[0,1],'Units Sold'] = np.nan
print(coffee.head())
print(coffee.isna().sum())
"""
Day            0
Coffee Type    0
Units Sold     2
dtype: int64
"""
coffee = coffee.fillna(coffee['Units Sold'].mean())
print(coffee.head())
coffee.loc[[2,3] , 'Units Sold'] = np.nan
print(coffee.head())
coffee['Units Sold'] = coffee['Units Sold'].interpolate()
print(coffee.head())
coffee.loc[[2,3],'Units Sold']=np.nan
print(coffee.dropna())
"""
0      Monday    Espresso        35.0
1      Monday       Latte        35.0
4   Wednesday    Espresso        35.0
5   Wednesday       Latte        25.0
6    Thursday    Espresso        40.0
7    Thursday       Latte        30.0
8      Friday    Espresso        45.0
9      Friday       Latte        35.0
10   Saturday    Espresso        45.0
11   Saturday       Latte        35.0
12     Sunday    Espresso        45.0
13     Sunday       Latte        35.0
"""
print(coffee[coffee['Units Sold'].isna()])
"""
       Day Coffee Type  Units Sold
2  Tuesday    Espresso         NaN
3  Tuesday       Latte         NaN
"""
print(coffee[coffee['Units Sold'].notna()])
"""
          Day Coffee Type  Units Sold
0      Monday    Espresso        35.0
1      Monday       Latte        35.0
4   Wednesday    Espresso        35.0
5   Wednesday       Latte        25.0
6    Thursday    Espresso        40.0
7    Thursday       Latte        30.0
8      Friday    Espresso        45.0
9      Friday       Latte        35.0
10   Saturday    Espresso        45.0
11   Saturday       Latte        35.0
12     Sunday    Espresso        45.0
13     Sunday       Latte        35.0
"""