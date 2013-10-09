import recipe
import brew
import hop
import grain
import yeast
import pickle

import unittest
import logging

class brew_test(unittest.TestCase):
    

    def test_function(self):
        log = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG)
        log.setLevel(logging.DEBUG)
        # log file handler
        logfile_handler = logging.FileHandler('test.test_function.log')
        logfile_handler.setLevel(logging.DEBUG)
        # add handlers to the logger
        log.addHandler(logfile_handler)
        log.debug('brew_test.test_function')


        #
        self.recipe = recipe.Recipe()


        # I modified select_ingredient to take programmatic input
        #self.recipe.select_ingredient('H')


        # But now I am going to try just appending to the lists
        # I forgot that the hops list is objects, not strings
        #self.recipe.hops = ['Select', 'Galaxy']


#        rob, this is an example of what comes out of the pkl file:
#            ['hops', {'name': '', 'aau': '3.2', 'hop': 'Galaxy', ...}
#        so we could pass stuff to select_ingredient like:
#            answer = item_from_pickeled_recipe[0]
#        self.recipe.hops = [hop.Hop()]


        brewing_session = brew.Brew(recipe)
        #brewing_session.loop()
        #print('test finished\n')
        log.debug('brew test function finished')

if __name__ == '__main__':
    unittest.main()

#mark, you said this stuff was trash now?
'''
i = []

<<<<<<< HEAD
=======
r = recipe.Recipe()
r.select_ingredient()
filename = open('test_recipe.pkl', 'wb')
#for thing in vars(r):
#    print thing
#    if not thing.startswith('date'):
#        for ingredient in eval('r.%s' % thing):
#            i.append(['%s' % thing, vars(ingredient)])

#for e in i:
#    print e
#pickle.dump(i, filename)
#filename.close()

recipe = pickle.load(filename)
        
for thing in vars(Recipe()):
    print thing

filename.close()

b = brew.Brew(r)

b.vourlaf()
b.start_timer()
b.loop()
print('test finished\n')
>>>>>>> 60f97891c14c2560277173f44be2273da8367b6d
'''
