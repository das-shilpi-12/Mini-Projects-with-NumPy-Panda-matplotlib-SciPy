import pandas as pd 
presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
print(presidents_df)
print("************************************************")
print("******************a******************************")
a = presidents_df.loc['Abraham Lincoln']
print(a)
print("************************************************")
print("*******************b*****************************")
b = presidents_df.loc['Abraham Lincoln' : 'Benjamin Harrison']
print(b)
print("************************************************")
print("*******************c*****************************")
c = type(presidents_df.loc['Abraham Lincoln'])
print(c)
print("************************************************")
print("*******************d*****************************")
d = presidents_df.iloc[11]
print(d)
print("************************************************")
print("*****************i*******************************")
i = presidents_df.iloc[11:20]
print(i)
print("************************************************")
print("*****************e*******************************")
e = presidents_df.columns
print(e)
print("************************************************")
print("*******************h*****************************")
h = presidents_df['age']
f = presidents_df['height'].shape
print(h)
print("******************f*****************************")
print(f)
print("*****************j***********************")
j = presidents_df[['height','age']].head(n=3)
print(j)
