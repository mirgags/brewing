from hop import *
from grain import *
from yeast import *
import pickle
from time import *


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
