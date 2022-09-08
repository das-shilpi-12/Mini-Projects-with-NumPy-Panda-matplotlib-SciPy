import pandas as pd 
print("*******Bill***************")
wine_dict = {
    'red-wine' : [1000,2000,3000],
    'white-wine' : [2800,9000,3400]
}
a = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"]) 
print(a)
print("**********************************************")
Food_price = {
    'pizza' : [300,346,789],
    'Burgur': [400,290,456],
    'Chawmin':[100,322,877]
}
b = pd.DataFrame(Food_price, index=["shilpi","Jin","Taehyung"])
print(b)
