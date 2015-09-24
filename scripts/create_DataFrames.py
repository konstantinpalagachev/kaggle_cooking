# import libraries
import pandas as pd
import os

# change working directory
os.chdir("/Users/kosta_pal/Desktop/DataAnalysis/Kaggle/Cooking/")

# read the data
train = pd.read_json("data/train.json")
test = pd.read_json("data/test.json")

# store individual ingredients for train and test datasets
allIngradients = set()
train.ingredients.map(lambda x: [allIngradients.add(i) for i in list(x)])
test.ingredients.map(lambda x: [allIngradients.add(i) for i in list(x)])

# create additional variables for each single ingredient in train and test dataset
i = 0
for ingredient in allIngradients:
    train[ingredient] = train.ingredients.map(lambda x: ingredient in x)
    test[ingredient] = test.ingredients.map(lambda x: ingredient in x)
    i += 1
    print(i,len(allIngradients))
    
# drop column ingredients
train.drop('ingredients', axis = 1, inplace = True)
test.drop('ingredients', axis = 1, inplace = True)

# save files to csv
train.to_csv("data/train.csv")
test.to_csv("data/test.csv")