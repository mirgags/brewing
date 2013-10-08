from hop import *
from grain import *
from yeast import *
import pickle
from time import *
from recipe import *
import thread


class Brew(object):


    def __init__(self, recipe):
        self.recipe = recipe
        self.volume = 0.0
        self.start_time = None 
        self.comments = []


    def volume_calc(self):
        while True:
            try:
                self.volume = float(raw_input("What will pre-boil volume be? > "))
                break
            except ValueError:
                print "Enter a decimal number for batch volume"


    def start_timer(self):
#        self.start_time = strftime("%H%M", localtime())
        self.start_time = time()


    def comment(self):
        self.comments.append([int((time() - self.start_time) / 60), raw_input("Type commments > ")])

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


    def mash(self):
        self.start_timer()
        a = True
        while a:
            timer = int((time() - self.start_time) / 60)          
            if timer % 20 == 0:
                print "check temp"
            print timer
            if timer > 60:
                a = False
            print "got to sleep"
            print a
            sleep(5)
        
        print "Mash out"

    def vourlaf(self):
        while True:
           try:
               runoff = float(raw_input("How much runoff? > " ))
               break
           except ValueError:
               print "Enter a decimal value. > "
        grain_lbs = 0
        for g in self.recipe.grains:
            grain_lbs = grain_lbs + g.lbs
        print grain_lbs
        print "vourlaf water is: %s" % ((7 - runoff) + (grain_lbs * .13))

    def loop(self):
        self.mash()
#        thread.start_new_thread(self.mash, ())
#        print "loop test"
#        thread.start_new_thread(self.comment, ())
#        print "comment running too"
