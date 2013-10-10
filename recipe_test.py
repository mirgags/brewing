from brew import *
import pickle

filename = open('test_recipe.pkl', 'rb')
test_recipe = pickle.load(filename)

for thing in test_recipe:
    print thing

