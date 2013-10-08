import recipe
import brew

import unittest

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
