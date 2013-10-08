import recipe
import brew
import hop
import grain
import yeast
import pickle

class my_test(unittest.TestCase):
    def test_function(self):
        #
        self.recipe = recipe.Recipe()
        # I modified select_ingredient to take programmatic input
        #self.recipe.select_ingredient('H')
        # But now I am going to try just appending to the lists
        # I forgot that the hops list is objects, not strings
        # hmm...zzz
        #self.recipe.hops = ['Select', 'Galaxy']
        brewing_session = brew.Brew(recipe)
        #brewing_session.loop()
        print('test finished\n')

if __name__ == '__main__':
    unittest.main()

#mark, you said this stuff was trash now?
'''
i = []

<<<<<<< HEAD
import unittest
=======
r = recipe.Recipe()
r.select_ingredient()
filename = open('test_recipe.pkl', 'wb')
for thing in vars(r):
    print thing
    if not thing.startswith('date'):
        for ingredient in eval('r.%s' % thing):
            i.append(['%s' % thing, vars(ingredient)])

#for e in i:
#    print e
pickle.dump(i, filename)
filename.close()
        
b = brew.Brew(r)
b.vourlaf()
b.start_timer()
b.loop()
print('test finished\n')
>>>>>>> 60f97891c14c2560277173f44be2273da8367b6d
'''
