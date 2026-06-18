import pandas as pd

coffee = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\warmup-data\coffee.csv")
bios = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\data\bios.csv")
# result = pd.read_parquet(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\data\results.parquet")
# olympics_data = pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\data\olympics-data.xlsx")

# print(coffee.head())
# """
#          Day Coffee Type  Units Sold
# 0     Monday    Espresso          25
# 1     Monday       Latte          15
# 2    Tuesday    Espresso          30
# 3    Tuesday       Latte          20
# 4  Wednesday    Espresso          35
# """
# print(coffee)
# """
#           Day Coffee Type  Units Sold
# 0      Monday    Espresso          25
# 1      Monday       Latte          15
# 2     Tuesday    Espresso          30
# 3     Tuesday       Latte          20
# 4   Wednesday    Espresso          35
# 5   Wednesday       Latte          25
# 6    Thursday    Espresso          40
# 7    Thursday       Latte          30
# 8      Friday    Espresso          45
# 9      Friday       Latte          35
# 10   Saturday    Espresso          45
# 11   Saturday       Latte          35
# 12     Sunday    Espresso          45
# 13     Sunday       Latte          35
# """
# print(coffee.columns) #  Index(['Day', 'Coffee Type', 'Units Sold'], dtype='str')
# print(coffee.describe())
# """
#        Units Sold
# count   14.000000
# mean    32.857143
# std      9.346798
# min     15.000000
# 25%     26.250000
# 50%     35.000000
# 75%     38.750000
# max     45.000000
# """
# print(coffee.info())
# """
# <class 'pandas.DataFrame'>
# RangeIndex: 14 entries, 0 to 13
# Data columns (total 3 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   Day          14 non-null     str  
#  1   Coffee Type  14 non-null     str  
#  2   Units Sold   14 non-null     int64
# dtypes: int64(1), str(2)
# memory usage: 468.0 bytes
# None
# """
# print(result)
# """
#           year    type  ...   tied medal
# 0       1912.0  Summer  ...   True   NaN
# 1       1912.0  Summer  ...  False   NaN
# 2       1920.0  Summer  ...   True   NaN
# 3       1920.0  Summer  ...   True   NaN
# 4       1920.0  Summer  ...  False   NaN
# ...        ...     ...  ...    ...   ...
# 308403  2022.0  Winter  ...  False   NaN
# 308404  2022.0  Winter  ...  False   NaN
# 308405  2022.0  Winter  ...  False   NaN
# 308406  2022.0  Winter  ...  False   NaN
# 308407  2022.0  Winter  ...  False   NaN

# [308408 rows x 11 columns]
# """
# print(result.info())
# """
# <class 'pandas.DataFrame'>
# RangeIndex: 308408 entries, 0 to 308407
# Data columns (total 11 columns):
#  #   Column      Non-Null Count   Dtype  
# ---  ------      --------------   -----  
#  0   year        305807 non-null  float64
#  1   type        305807 non-null  str    
#  2   discipline  308407 non-null  str    
#  3   event       308408 non-null  str    
#  4   as          308408 non-null  str    
#  5   athlete_id  308408 non-null  int64  
#  6   noc         308407 non-null  str    
#  7   team        121714 non-null  str    
#  8   place       283193 non-null  float64
#  9   tied        308408 non-null  bool   
#  10  medal       44139 non-null   str    
# dtypes: bool(1), float64(2), int64(1), str(7)
# memory usage: 46.0 MB
# None
# """
# print(olympics_data)
# """
#         athlete_id                   name   born_date        born_city           born_region born_country        NOC  height_cm  weight_kg   died_date
# 0                1  Jean-François Blanchy  1886-12-12         Bordeaux               Gironde          FRA     France        NaN        NaN  1960-10-02
# 1                2         Arnaud Boetsch  1969-04-01           Meulan              Yvelines          FRA     France      183.0       76.0         NaN
# 2                3           Jean Borotra  1898-08-13         Biarritz  Pyrénées-Atlantiques          FRA     France      183.0       76.0  1994-07-17
# 3                4        Jacques Brugnon  1895-05-11      Paris VIIIe                 Paris          FRA     France      168.0       64.0  1978-03-20
# 4                5           Albert Canet  1878-04-17       Wandsworth               England          GBR     France        NaN        NaN  1930-07-25
# ...            ...                    ...         ...              ...                   ...          ...        ...        ...        ...         ...
# 145495      149222      Polina Luchnikova  2002-01-30            Serov            Sverdlovsk          RUS        ROC      167.0       61.0         NaN
# 145496      149223    Valeriya Merkusheva  1999-09-20  Moskva (Moscow)                Moskva          RUS        ROC      168.0       65.0         NaN
# 145497      149224        Yuliya Smirnova  1998-05-08           Kotlas           Arkhangelsk          RUS        ROC      163.0       55.0         NaN
# 145498      149225         André Foussard  1899-05-19            Niort           Deux-Sèvres          FRA     France      166.0        NaN  1986-03-18
# 145499      149814          Bill Phillips  1913-07-15     Dulwich Hill       New South Wales          AUS  Australia        NaN        NaN  2003-10-20

# [145500 rows x 10 columns]
# """
# print(bios.to_excel)
# print(coffee.sample(5))
# """
#          Day Coffee Type  Units Sold
# 7   Thursday       Latte          30
# 1     Monday       Latte          15
# 10  Saturday    Espresso          45
# 12    Sunday    Espresso          45
# 6   Thursday    Espresso          40
# """
# print(coffee.loc[0])
# """
# Day              Monday
# Coffee Type    Espresso
# Units Sold           25
# Name: 0, dtype: object
# """
# print(coffee.loc[[0,1,5]])
# """
#          Day Coffee Type  Units Sold
# 0     Monday    Espresso          25
# 1     Monday       Latte          15
# 5  Wednesday       Latte          25
# """
# print(coffee.loc[0:3])
# """
#        Day Coffee Type  Units Sold
# 0   Monday    Espresso          25
# 1   Monday       Latte          15
# 2  Tuesday    Espresso          30
# 3  Tuesday       Latte          20
# """
# print(coffee.loc[:8,["Day","Units Sold"]])
# """
#          Day  Units Sold
# 0     Monday          25
# 1     Monday          15
# 2    Tuesday          30
# 3    Tuesday          20
# 4  Wednesday          35
# 5  Wednesday          25
# 6   Thursday          40
# 7   Thursday          30
# 8     Friday          45
# """
# print(coffee.iloc[0:8,[0,2]])
# """
#          Day  Units Sold
# 0     Monday          25
# 1     Monday          15
# 2    Tuesday          30
# 3    Tuesday          20
# 4  Wednesday          35
# 5  Wednesday          25
# 6   Thursday          40
# 7   Thursday          30
# """
# coffee.loc[1,"Units Sold"]=10
# print(coffee.head(2))
# """
# 0  Monday    Espresso          25
# 1  Monday       Latte          10
# """
# coffee.loc[0:3,"Units Sold"] = 5
# print(coffee.head(3))
# """
#        Day Coffee Type  Units Sold
# 0   Monday    Espresso           5
# 1   Monday       Latte           5
# 2  Tuesday    Espresso           5
# """
## coffee.at[row_lable,column_lable]
# print(coffee.at[0,"Day"]) # Monday
# print(coffee.iat[0,0])
# """
# Monday
# Monday
# """
# print(coffee.sort_values("Units Sold"))
# """
#           Day Coffee Type  Units Sold
# 1      Monday       Latte          15
# 3     Tuesday       Latte          20
# 0      Monday    Espresso          25
# 5   Wednesday       Latte          25
# 2     Tuesday    Espresso          30
# 7    Thursday       Latte          30
# 4   Wednesday    Espresso          35
# 9      Friday       Latte          35
# 13     Sunday       Latte          35
# 11   Saturday       Latte          35
# 6    Thursday    Espresso          40
# 8      Friday    Espresso          45
# 10   Saturday    Espresso          45
# 12     Sunday    Espresso          45
# """
# print(coffee.sort_values("Units Sold",ascending=False))
# """
#           Day Coffee Type  Units Sold
# 10   Saturday    Espresso          45
# 8      Friday    Espresso          45
# 12     Sunday    Espresso          45
# 6    Thursday    Espresso          40
# 4   Wednesday    Espresso          35
# 11   Saturday       Latte          35
# 13     Sunday       Latte          35
# 9      Friday       Latte          35
# 2     Tuesday    Espresso          30
# 7    Thursday       Latte          30
# 0      Monday    Espresso          25
# 5   Wednesday       Latte          25
# 3     Tuesday       Latte          20
# 1      Monday       Latte          15
# """
# # you can pass two parameter to sort values
# print(coffee.sort_values(["Units Sold","Day"],ascending=[0,1]))
# # here frst priority is unit sold which is decending order then day which is in ascending order
# print(coffee.iterrows())
# # iterrows() is a Pandas function that allows you to loop through each row of a DataFrame one by one.
# for index , row in coffee.iterrows():
#     print(index)
#     print(row)
#     print("\n")
# """
# 0
# Day              Monday
# Coffee Type    Espresso
# Units Sold           25
# Name: 0, dtype: object


# 1
# Day            Monday
# Coffee Type     Latte
# Units Sold         15
# Name: 1, dtype: object


# 2
# Day             Tuesday
# Coffee Type    Espresso
# Units Sold           30
# Name: 2, dtype: object


# 3
# Day            Tuesday
# Coffee Type      Latte
# Units Sold          20
# Name: 3, dtype: object


# 4
# Day            Wednesday
# Coffee Type     Espresso
# Units Sold            35
# Name: 4, dtype: object


# 5
# Day            Wednesday
# Coffee Type        Latte
# Units Sold            25
# Name: 5, dtype: object


# 6
# Day            Thursday
# Coffee Type    Espresso
# Units Sold           40
# Name: 6, dtype: object


# 7
# Day            Thursday
# Coffee Type       Latte
# Units Sold           30
# Name: 7, dtype: object


# 8
# Day              Friday
# Coffee Type    Espresso
# Units Sold           45
# Name: 8, dtype: object


# 9
# Day            Friday
# Coffee Type     Latte
# Units Sold         35
# Name: 9, dtype: object


# 10
# Day            Saturday
# Coffee Type    Espresso
# Units Sold           45
# Name: 10, dtype: object


# 11
# Day            Saturday
# Coffee Type       Latte
# Units Sold           35
# Name: 11, dtype: object


# 12
# Day              Sunday
# Coffee Type    Espresso
# Units Sold           45
# Name: 12, dtype: object


# 13
# Day            Sunday
# Coffee Type     Latte
# Units Sold         35
# Name: 13, dtype: object


# """
# print(bios.loc[bios["height_cm"]>220,["name","height_cm"]])
# """
#                    name  height_cm
# 5673     Gunther Behnke      221.0
# 5781     Tommy Burleson      223.0
# 6978    Arvydas Sabonis      223.0
# 89070          Yao Ming      226.0
# 89075    Roberto Dueñas      221.0
# 120266     Zhang Zhaoxu      221.0
# """
# print(bios[bios["height_cm"]>220][["name","height_cm"]])
# """
#                    name  height_cm
# 5673     Gunther Behnke      221.0
# 5781     Tommy Burleson      223.0
# 6978    Arvydas Sabonis      223.0
# 89070          Yao Ming      226.0
# 89075    Roberto Dueñas      221.0
# 120266     Zhang Zhaoxu      221.0
# """
# print(bios[(bios["height_cm"]>215 )& (bios["born_country"]=="USA")])
# print(bios[bios["name"].str.contains("keith|patrick",case=False)])
print(bios[bios["born_country"].isin(["USA","FRA","GBR"]) | (bios["name"].str.startswith("keith"))])
print(bios.query('born_country == "USA" and born_city == "Seattle"'))
# .query() is a Pandas method used to filter rows of a DataFrame using a string expression.
coffee['price']=4.99
print(coffee.head())
""""
         Day Coffee Type  Units Sold  price
0     Monday    Espresso          25   4.99
1     Monday       Latte          15   4.99
2    Tuesday    Espresso          30   4.99
3    Tuesday       Latte          20   4.99
4  Wednesday    Espresso          35   4.99
"""
import numpy as np
coffee['new_price'] = np.where(coffee['Coffee Type']=="Espresso",3.99,5.99)
print(coffee.head())
"""
         Day Coffee Type  Units Sold  price  new_price
0     Monday    Espresso          25   4.99       3.99
1     Monday       Latte          15   4.99       5.99
2    Tuesday    Espresso          30   4.99       3.99
3    Tuesday       Latte          20   4.99       5.99
4  Wednesday    Espresso          35   4.99       3.99
"""
print(coffee.drop([0,1,2,5]))
"""
          Day Coffee Type  Units Sold  price  new_price
3     Tuesday       Latte          20   4.99       5.99
4   Wednesday    Espresso          35   4.99       3.99
6    Thursday    Espresso          40   4.99       3.99
7    Thursday       Latte          30   4.99       5.99
8      Friday    Espresso          45   4.99       3.99
9      Friday       Latte          35   4.99       5.99
10   Saturday    Espresso          45   4.99       3.99
11   Saturday       Latte          35   4.99       5.99
12     Sunday    Espresso          45   4.99       3.99
13     Sunday       Latte          35   4.99       5.99
"""
print(coffee.drop(columns=["price"]))
"""
          Day Coffee Type  Units Sold  new_price
0      Monday    Espresso          25       3.99
1      Monday       Latte          15       5.99
2     Tuesday    Espresso          30       3.99
3     Tuesday       Latte          20       5.99
4   Wednesday    Espresso          35       3.99
5   Wednesday       Latte          25       5.99
6    Thursday    Espresso          40       3.99
7    Thursday       Latte          30       5.99
8      Friday    Espresso          45       3.99
9      Friday       Latte          35       5.99
10   Saturday    Espresso          45       3.99
11   Saturday       Latte          35       5.99
12     Sunday    Espresso          45       3.99
13     Sunday       Latte          35       5.99
"""
print(coffee.head())
"""
         Day Coffee Type  Units Sold  price  new_price
0     Monday    Espresso          25   4.99       3.99
1     Monday       Latte          15   4.99       5.99
2    Tuesday    Espresso          30   4.99       3.99
3    Tuesday       Latte          20   4.99       5.99
4  Wednesday    Espresso          35   4.99       3.99
"""
coffee_new = coffee.copy()
coffee_new["price"] = 5.99
print(coffee_new.head())
"""
         Day Coffee Type  Units Sold  price  new_price
0     Monday    Espresso          25   5.99       3.99
1     Monday       Latte          15   5.99       5.99
2    Tuesday    Espresso          30   5.99       3.99
3    Tuesday       Latte          20   5.99       5.99
4  Wednesday    Espresso          35   5.99       3.99
"""
coffee_new=coffee_new.drop(columns=["price"])
print(coffee_new.head())
"""
         Day Coffee Type  Units Sold  new_price
0     Monday    Espresso          25       3.99
1     Monday       Latte          15       5.99
2    Tuesday    Espresso          30       3.99
3    Tuesday       Latte          20       5.99
4  Wednesday    Espresso          35       3.99
"""
coffee_new['revenue'] = coffee_new['Units Sold'] * coffee_new['new_price']
print(coffee_new.head())
"""
         Day Coffee Type  Units Sold  new_price  revenue
0     Monday    Espresso          25       3.99    99.75
1     Monday       Latte          15       5.99    89.85
2    Tuesday    Espresso          30       3.99   119.70
3    Tuesday       Latte          20       5.99   119.80
4  Wednesday    Espresso          35       3.99   139.65
"""
print(coffee_new.rename(columns={'new_price':'price'}).head())
"""
         Day Coffee Type  Units Sold  new_price  revenue
0     Monday    Espresso          25       3.99    99.75
1     Monday       Latte          15       5.99    89.85
2    Tuesday    Espresso          30       3.99   119.70
3    Tuesday       Latte          20       5.99   119.80
4  Wednesday    Espresso          35       3.99   139.65
"""
bios_new=bios.copy()
bios_new['first_name'] = bios_new["name"].str.split(' ').str[0]
print(bios_new.head())
"""
   athlete_id                   name   born_date  ... weight_kg   died_date     first_name
0           1  Jean-François Blanchy  1886-12-12  ...       NaN  1960-10-02  Jean-François
1           2         Arnaud Boetsch  1969-04-01  ...      76.0         NaN         Arnaud
2           3           Jean Borotra  1898-08-13  ...      76.0  1994-07-17           Jean
3           4        Jacques Brugnon  1895-05-11  ...      64.0  1978-03-20        Jacques
4           5           Albert Canet  1878-04-17  ...       NaN  1930-07-25         Albert
"""
bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'] , format="%Y-%m-%d")
print(bios_new.head())
"""
   athlete_id                   name  ...     first_name born_datetime
0           1  Jean-François Blanchy  ...  Jean-François    1886-12-12
1           2         Arnaud Boetsch  ...         Arnaud    1969-04-01
2           3           Jean Borotra  ...           Jean    1898-08-13
3           4        Jacques Brugnon  ...        Jacques    1895-05-11
4           5           Albert Canet  ...         Albert    1878-04-17
"""
bios_new['born_year'] = bios_new['born_datetime'].dt.year
print(bios_new[["name","born_year"]].head())
"""
                    name  born_year
0  Jean-François Blanchy     1886.0
1         Arnaud Boetsch     1969.0
2           Jean Borotra     1898.0
3        Jacques Brugnon     1895.0
4           Albert Canet     1878.0
"""
bios_new.to_csv(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\rudra.csv" , index = False)
bios["height_category"] = bios["height_cm"].apply(lambda x: 'short' if x < 165 else ('average' if x < 185 else 'tall'))
print(bios[["height_cm","height_category"]])
"""
        height_cm height_category
0             NaN            tall
1           183.0         average
2           183.0         average
3           168.0         average
4             NaN            tall
...           ...             ...
145495      167.0         average
145496      168.0         average
145497      163.0           short
145498      166.0         average
145499        NaN            tall
"""
def categorize_athlete(row):
    if row['height_cm'] < 175 and row['weight_kg'] < 70:
        return 'Lightweight'
    elif row['height_cm'] < 185 or row['weight_kg'] <=80:
        return 'Middleweight'
    else :
        return 'Heavyweight'
    
bios['category'] = bios.apply(categorize_athlete,axis=1)
"""
apply():
apply() runs a function on a DataFrame.
axis=1 means:
Apply the function row by row
"""
print(bios['category'].head())
"""
0     Heavyweight
1    Middleweight
2    Middleweight
3     Lightweight
4     Heavyweight
"""