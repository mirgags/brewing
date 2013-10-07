from hop import *
from grain import *
from yeast import *
import pickle
from time import *
from recipe import *


class Brew(object):


    def __init__(self, recipe):
        self.recipe = recipe
        self.volume = 0.0
        self.start_time = 0.0 
        self.comments = []


    def volume_calc(self):
        while True:
            try:
                self.volume = float(raw_input("What will pre-boil volume be? > "))
                break
            except ValueError:
                print "Enter a decimal number for batch volume"


    def start_brew(self):
        self.start_time = strftime("%H%M", localtime())


    def comment(self):
        self.comments.append([strftime("%H%M", localtime()), raw_input("Type commments > ")])

    def printer(self):
        for i in self.comments:
            print(i)

    def target_gravity(self):
        gravity = 0
        for g in self.recipe.grains:
            if g.gravity != ("" or None):
                gravity = gravity + ((g.gravity * g.lbs) / self.volume)
            else:
                while True:
                    try:
                        gravity = gravity + (float(raw_input("No saved gravity for %s, please enter. > " % g.grain)) / self.volume)
                        break
                    except ValueError:
                        print "Enter a decimal value. > "
        return gravity



    def grain_absorbtion(self, lbs):
        self.lbs = lbs
        return (lbs * 1.25 / 4)




