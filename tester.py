import recipe
import brew

r = recipe.Recipe()
b = brew.Brew(r)
b.start_brew2()
b.comment('test comment')
b.printer()
print('test finished\n')
