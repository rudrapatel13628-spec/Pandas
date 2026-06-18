import pandas as pd
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["A","B","C"],index=["X","Y","Z"])
print(df.head())
"""    A  B  C
    X  1  2  3
    Y  4  5  6
    Z  7  8  9      """
print(df.head(1))
"""    A  B  C
    X  1  2  3      """
print(df.head(2))
"""    A  B  C
    X  1  2  3
    Y  4  5  6      """
print(df.tail(1))
"""    A  B  C
    Z  7  8  9       """
print(df.columns)  #  Index(['A', 'B', 'C'], dtype='str')
print(df.index)  #  Index(['X', 'Y', 'Z'], dtype='str')
print(df)
"""    A  B  C
    X  1  2  3
    Y  4  5  6
    Z  7  8  9      """
print(df.info())
"""
<class 'pandas.DataFrame'>
Index: 3 entries, X to Z
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   A       3 non-null      int64
 1   B       3 non-null      int64
 2   C       3 non-null      int64
dtypes: int64(3)
memory usage: 96.0+ bytes
None
"""
print(df.describe())
"""
         A    B    C
count  3.0  3.0  3.0
mean   4.0  5.0  6.0
std    3.0  3.0  3.0
min    1.0  2.0  3.0
25%    2.5  3.5  4.5
50%    4.0  5.0  6.0
75%    5.5  6.5  7.5
max    7.0  8.0  9.0
"""
print(df.nunique()) 
""" A    3
    B    3
    C    3
    dtype: int64    """
print(df['A'].unique()) #  [1 4 7]
print(df.shape)  #  (3, 3)
print(df.size)  #  9