import recipe
import brew

r = recipe.Recipe()
b = brew.Brew(r)
b.loop()
print('test finished\n')

