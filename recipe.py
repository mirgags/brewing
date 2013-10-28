from hop import *
from grain import *
from yeast import *
import pickle
from time import *
import os
import sys


class Recipe(object):


    def __init__(self):
        self.date = strftime("%m-%d-%Y", localtime())
        self.grains = []
        self.hops = []
        self.yeast = []


    def grain_absorbtion(self, lbs):
        self.lbs = lbs
        return (lbs * 1.25 / 4)

    #this is in the brew class now, correct?
    #yes rob, this is in brew (we can delete) - Mark
#    def start_brew(self):
#        start_time = localtime()


    def select_ingredient(self, test_input=None):
        if test_input == None:
            print "Add ingredients or type \"Done\" to finish."
            answer = raw_input("Is this a hop, grain or yeast? > ").upper()
            while not any(answer.startswith(let) for let in ["D", "H", "G", "Y"]):
                print "That's not a beer ingredient, try again or \"Done\" > "
                self.select_ingredient()
            if answer.startswith("H"):
                ingredient = Hop(raw_input("What is the name? > "))
                ingredient.ounces = float(raw_input("How many ounces? > "))
                self.hops.append(ingredient)
            if answer.startswith("G"):
                ingredient = Grain(raw_input("What is the name? > "))
                ingredient.lbs = float(raw_input("How many pounds? >"))
                self.grains.append(ingredient)
            if answer.startswith("Y"):
                ingredient = Yeast(raw_input("What is the name? > "))
                self.yeast.append(ingredient)

        else:
            answer = test_input[0]
            if answer.startswith("H"):
                ingredient = Hop()
                for key in vars(ingredient):
                    'ingredient.%s = test_input[0][%s]' % key, key
                self.hops.append(ingredient)
            if answer.startswith("G"):
                ingredient = Grain()
                for key in vars(ingredient):
                    'ingredient.%s = test_input[0][%s]' % key, key
                self.grains.append(ingredient)
            if answer.startswith("Y"):
                ingredient = Yeast()
                for key in vars(ingredient):
                    'ingredient.%s = test_input[0][%s]' % key, key
                self.yeast.append(ingredient)
           
#        if not answer.startswith("D"):
            print "Hops >"
            for el in self.hops:
                print el.hop
            print "Grains >"
            for el in self.grains:
                print el.grain
            print "Yeast >"
            for el in self.yeast:
                print el.yeast
            self.select_ingredient()


    def save_recipe(self, *args):
#   example of output: {'name': string, ['hops'/'grains'/'yeast', objectvars]}
        i = []
        recipe_list = {}
        r = self
        if args:
            if args.count() == 1:
                r_name = args[0]
            else:
                print("Too many recipe arguments.  Exiting.")
                sys.exit()
        else:
            r_name = raw_input("Name this recipe > ")
        filename = open('test_recipe.pkl', 'rb')
        while True:
            try:
                recipe_list = pickle.load(filename)
                filename.close()
                break
            except EOFError:
                break

        if r_name in recipe_list:
            answer = raw_input("%s already exists, do you want to overwrite? (y/n)" % r_name)
            if answer.startswith("N"):
                print("Exiting, not updated")
                sys.exit()

        for thing in vars(r): 
            #print thing
            if not thing.startswith('date'):
                for ingredient in eval("r.%s" % thing):
                    i.append(['%s' % thing, vars(ingredient)])

        filename = open('test_recipe.pkl', 'wb')
        recipe_list[r_name] =  i
        pickle.dump(recipe_list, filename)
        filename.close()


    def get_recipe(self, recipe_name):
        self.recipe_name = recipe_name
        filename = open('test_recipe.pkl', 'rb')
        recipe_list = pickle.load(filename)
        filename.close()
        for key in recipe_list:
            print key
            print recipe_list[key]
            
            if key.startswith(recipe_name):
                for thing in recipe_list[key]:
                    print thing[0]
                    print thing[1]
                    if thing[0].startswith('hop'):
                        self.hops.append(Hop())
                        self.hops[len(self.hops) - 1].name = thing[1]['name']
                        self.hops[len(self.hops) - 1].aau = thing[1]['aau']
                        self.hops[len(self.hops) - 1].hop = thing[1]['hop']
                        self.hops[len(self.hops) - 1].origin = thing[1]['origin']
                        self.hops[len(self.hops) - 1].character = thing[1]['character']
                        self.hops[len(self.hops) - 1].add_time = thing[1]['add_time']
                        self.hops[len(self.hops) - 1].ounces = thing[1]['ounces']
#                        for ingredient in vars(thing[1]):
#                            eval("self.hops[len(self.hops)].%s = recipe_list[key][1][%s]" % (ingredient, ingredient))
                    if thing[0].startswith('grain'):
                        self.grains.append(Grain())
                        self.grains[len(self.grains) - 1].name = thing[1]['name']
                        self.grains[len(self.grains) - 1].lovibond = thing[1]['lovibond']
                        self.grains[len(self.grains) - 1].grain = thing[1]['grain']
                        self.grains[len(self.grains) - 1].gravity = thing[1]['gravity']
                        self.grains[len(self.grains) - 1].character = thing[1]['character']
                        self.grains[len(self.grains) - 1].lbs = thing[1]['lbs']
                       
#                        for ingredient in vars(thing[1]):
#                            eval("self.grains[len(self.grains)].%s = recipe_list[key][1][%s]" % (ingredient, ingredient))
                    if thing[0].startswith('yeast'):
                        self.yeast.append(Yeast())
                        self.yeast[len(self.yeast) - 1].name = thing[1]['name']
                        self.yeast[len(self.yeast) - 1].producer = thing[1]['producer']
                        self.yeast[len(self.yeast) - 1].yeast = thing[1]['yeast']
                        self.yeast[len(self.yeast) - 1].id_code = thing[1]['id_code']
                        self.yeast[len(self.yeast) - 1].attenuation = thing[1]['attenuation']
                        self.yeast[len(self.yeast) - 1].flocculation = thing[1]['flocculation']
                        self.yeast[len(self.yeast) - 1].ferment_temp = thing[1]['ferment_temp']
                        self.yeast[len(self.yeast) - 1].alcohol_yield = thing[1]['alcohol_yield']
                        self.yeast[len(self.yeast) - 1].pitch_temp = thing[1]['pitch_temp']
 
#                        for ingredient in vars(thing[1]):
#                            eval("self.yeast[len(self.yeast)].%s = recipe_list[key][1][%s]" % (ingredient, ingredient))





#when uncommented, this script will add a recipe loop to storage
##########
if __name__ == "__main__":
    test_recipe = Recipe()
    q = True
    while q:
        test_recipe.select_ingredient()
        if raw_input('More? y/n > ').upper() == "N":
            q = False
    test_recipe.save_recipe()

