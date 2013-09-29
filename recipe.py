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


    def start_brew(self):
        start_time = localtime()


    def select_ingredient(self):
        print "Add ingredients or type \"Done\" to finish."
        answer = raw_input("Is this a hop, grain or yeast? > ").upper()
        if not answer.startswith("D"):
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
