import recipe
import brew
import hop
import grain
import yeast
import pickle

i = []

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

