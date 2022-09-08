import pandas as pd 
presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
print("info = ",presidents_df.info())
