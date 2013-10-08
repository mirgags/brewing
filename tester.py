import recipe
import brew

import unittest

class my_test(unittest.TestCase):
    def test_function(self):
        self.recipe = recipe.Recipe()
        brewing_session = brew.Brew(recipe)
        brewing_session.loop()
        print('test finished\n')

if __name__ == '__main__':
    unittest.main()
