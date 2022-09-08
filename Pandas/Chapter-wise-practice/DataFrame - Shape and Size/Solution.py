#Inspect a DataFrame - Shape and Size
import pandas as pd 
presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
print(presidents_df)
print("*********************")
print("Shape = ",presidents_df.shape)
print("*********************")
print("Size = ",presidents_df.size)
print("*********************")
print("Shape[0] = ",presidents_df.shape[0])
print("Shape[1] = ",presidents_df.shape[1])
