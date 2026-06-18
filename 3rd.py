import pandas as pd
bios = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\data\bios.csv")
nocs = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\data\noc_regions.csv")
print(nocs.head())
print(bios.head())
# bios_new=pd.merge(bios,nocs,left_on='born_country',right_on='NOC',how='left')
# print(bios_new.head())
"""
   athlete_id                   name   born_date    born_city           born_region born_country   NOC_x  height_cm  weight_kg   died_date NOC_y  region notes
0           1  Jean-François Blanchy  1886-12-12     Bordeaux               Gironde          FRA  France        NaN        NaN  1960-10-02   FRA  France   NaN
1           2         Arnaud Boetsch  1969-04-01       Meulan              Yvelines          FRA  France      183.0       76.0         NaN   FRA  France   NaN
2           3           Jean Borotra  1898-08-13     Biarritz  Pyrénées-Atlantiques          FRA  France      183.0       76.0  1994-07-17   FRA  France   NaN
3           4        Jacques Brugnon  1895-05-11  Paris VIIIe                 Paris          FRA  France      168.0       64.0  1978-03-20   FRA  France   NaN
4           5           Albert Canet  1878-04-17   Wandsworth               England          GBR  France        NaN        NaN  1930-07-25   GBR      UK   NaN
"""
# after add suffixes NOC_x and NOC_y change 
bios_new = pd.merge(bios,nocs,left_on='born_country',right_on='NOC',how='left',suffixes=["bios","nocdf"])
bios_new.rename(columns={'region':'born_country_full'},inplace=True)
print(bios_new.head())
"""
   athlete_id                   name   born_date    born_city           born_region born_country NOCbios  height_cm  weight_kg   died_date NOCnocdf born_country_full notes
0           1  Jean-François Blanchy  1886-12-12     Bordeaux               Gironde          FRA  France        NaN        NaN  1960-10-02      FRA            France   NaN
1           2         Arnaud Boetsch  1969-04-01       Meulan              Yvelines          FRA  France      183.0       76.0         NaN      FRA            France   NaN
2           3           Jean Borotra  1898-08-13     Biarritz  Pyrénées-Atlantiques          FRA  France      183.0       76.0  1994-07-17      FRA            France   NaN
3           4        Jacques Brugnon  1895-05-11  Paris VIIIe                 Paris          FRA  France      168.0       64.0  1978-03-20      FRA            France   NaN
4           5           Albert Canet  1878-04-17   Wandsworth               England          GBR  France        NaN        NaN  1930-07-25      GBR                UK   NaN
"""
"""
With inplace=True:
It modifies the original DataFrame directly.

bios_new.rename(columns={'region': 'born_country_full'}, inplace=True)

Result:
bios_new is updated

Without inplace=True:
It does not change the original DataFrame.
It returns a new DataFrame with the renamed column.

new_data = bios_new.rename(columns={'region': 'born_country_full'})
Result:
new_data has the renamed column,
but the original bios_new remains unchanged.
"""
usa = bios[bios['born_country']=='USA'].copy()
gbr = bios[bios['born_country']=='GBR'].copy()
print(usa.head())
print(gbr.head())
new_df = pd.concat([usa,gbr])
print(new_df.head())
print(new_df.tail())
results = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Panda\complete-pandas-tutorial\data\results.csv")
combined_df = pd.merge(results,bios,on='athlete_id',how = 'left')
print(combined_df.head())
"""
[5 rows x 10 columns]
     year    type  ... weight_kg   died_date
0  1912.0  Summer  ...       NaN  1960-10-02
1  1912.0  Summer  ...       NaN  1960-10-02
2  1920.0  Summer  ...       NaN  1960-10-02
3  1920.0  Summer  ...       NaN  1960-10-02
4  1920.0  Summer  ...       NaN  1960-10-02
"""