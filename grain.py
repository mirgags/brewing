import pickle
import time


class Grain(object):

    def __init__(self, *args):
        if len(args) > 0:
            if len(args) == 1:
                if raw_input("Do you want to use stored grain attributes? (y/n) > ").upper() == "Y":
                    grain_list = [args[0]]
                    self.select_grain(grain_list)
                    self.lovibond = self.lovibond()
                    self.gravity = self.gravity()
                    self.character = self.character()
                    self.name = args[0]
                    print "Object: %s created." % args[0]
            else:
                self.grain = ""
                print "Too many arguments, no attributes set."
        else:
            print "Empty object created."
            self.name = ""
            self.grain = ""
            self.lovibond = ""
            self.gravity = ""
            self.character = ""
        self.lbs = ""
       

    def read_grainfile(self):
        filename = open('grain_list.pkl', 'rb')
        hashed_grains = pickle.load(filename)
        filename.close()
        return hashed_grains


    def write_grainfile(self, grains_dict):
        filename = open('grain_list.pkl', 'wb')
        pickle.dump(grains_dict, filename)
        filename.close()


    def add_grain(self):
        if self.grain == "":
            self.grain = raw_input("what do you want to call it? > ")
        else:
            if raw_input("Do you want to call it %s? (y/n) > " % self.grain).upper() != "Y":
                self.grain = ""
                self.add_grain()
        if self.lovibond == "":
            grain_lovibond = raw_input("what is the lovibond rating, fool? > ")
        else:
            grain_lovibond = self.lovibond 
        if self.gravity == "":
            grain_gravity = raw_input("What is the gravity? > ")
        else:
            grain_gravity = self.gravity
        if self.character == "":
            grain_character = raw_input("Got any clever comments about it? > ")
        else:
            grain_character = self.character
        hashed_grains = self.read_grainfile()
        hashed_grains[self.grain] = ({'lovibond': grain_lovibond,
                                     'gravity': grain_gravity,
                                     'character': grain_character})
        self.write_grainfile(hashed_grains)

        ###Do I want to return the added values to the object?
        #for key in self.__dict__.keys():
        #    self.__dict__[key] = hashed_grains[self.grain][key]

        return "Created: ", (self.grain, grain_lovibond, grain_gravity)

    def remove_grain(self):
        grain_key = []
        if self.grain == "":
            grain_key.append(raw_input("what grain do you want to remove? > "))
        else:
            grain_key.append(self.grain)
            self.select_grain(grain_key)
        hashed_grains = self.read_grainfile()
        if self.grain in hashed_grains:
            print ("Are you sure you want to remove: %s?"
                   % hashed_grains[self.grain])
            answer = raw_input("(y/n) > ")
            if answer.upper() == ("Y"):
                del hashed_grains[self.grain]
                self.write_grainfile(hashed_grains)
                print "%s deleted." % self.grain
                for key in self.__dict__.keys():
                    self.__dict__[key] = ""
            else:
                print "%s not deleted." %self.grain
        else:
            print "Not found in list."


    def select_grain(self, myList = [], *args):
        hashed_grains = self.read_grainfile()
        input_list = []
        for x in myList:
            input_list.append(x)
        if len(input_list) >= 2:
            print "That could be any  of these:"
            for i in range(0, len(input_list) - 1):
                print "%s > %s" % (i, input_list[i])

            answer = raw_input("""Which one is it? (Type a string to search
                               again) > """)
            while True:
                try:
                    number = int(answer)
                    is_integer = True
                    break
                except ValueError:
                    is_integer = False
                    break
            if is_integer: 
                input_list = [input_list[number]]
            else:
                input_list = []
                input_list.append(answer)
            self.select_grain(input_list)
           
        elif len(input_list) == 1:
            output_list = []
            for key in hashed_grains:
                if input_list[0].upper() == key.upper():
                    print input_list[0]
                    if raw_input("Is it this one? (y/n) > ").upper() == "Y":
                        self.grain = "%s" % input_list[0]
                        return
                elif input_list[0].upper() in key.upper():
                    output_list.append(key)
            if not output_list:
                if raw_input("Don\'t have that grain. Want to add it? (y/n) > "
                            ).upper() == "Y":
                    self.add_grain()
                else:
                    return "Grain not added."
            self.select_grain(output_list)


    def edit_grains(self):
        hashed_grains = self.read_grainfile()
        for key in hashed_grains:
            print "%s, gravity: %s" % (key, hashed_grains[key]['gravity'])
            hashed_grains[key]['gravity'] = float(raw_input("enter gravity > "))
        self.write_grainfile(hashed_grains)

    def grain(self):
        arguments = [raw_input("what grain is this? > ")]
        self.select_grain(arguments)
        return self.grain

    def lovibond(self):
        hashed_grains = self.read_grainfile()
        self.lovibond = hashed_grains[self.grain]['lovibond']
        return hashed_grains[self.grain]['lovibond']


    def gravity(self):
        hashed_grains = self.read_grainfile()
        self.gravity = hashed_grains[self.grain]['gravity']
        return hashed_grains[self.grain]['gravity']


    def character(self):
        hashed_grains = self.read_grainfile()
        self.character = hashed_grains[self.grain]['character']
        return hashed_grains[self.grain]['character']

