import pandas as pd

# creation
# create df with the given columns
df = pd.DataFrame(np.nan, index=[], columns=['Source','Target','Label','Weight'])

# create totally emtpry dataframe
pd.DataFrame(np.nan, index=[], columns=[])

# fill data in

# set cell, no matter if the row or column exists, it will be created
df.set_value(row,"column",value)
# to add as last row
df.set_value(len(df.index),"column",value)



# iteration
# iterate over dataframe
for index, row in df.iterrows():

# access rows
row["column_name"]




# slicing
df_outer = df[0:1]


# print

print(b.describe())
print(b.info())
# print full dataframe
print(b)
