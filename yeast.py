import pickle
import time


class Yeast(object):

    def __init__(self, *args):
        if len(args) > 0:
            if len(args) == 1:
                if raw_input("Do you want to use stored yeast attributes? (y/n) > ").upper() == "Y":
                    yeast_list = [args[0]]
                    self.select_yeast(yeast_list)
                    self.producer = self.producer()
                    self.id_code = self.id_code()
                    self.attenuation = self.attenuation()
                    self.flocculation = self.flocculation()
                    self.ferment_temp = self.ferment_temp()
                    self.alcohol_yield = self.alcohol_yield()
                    self.name = args[0]
                    print "Object: %s created." % args[0]
            else:
                self.yeast = ""
                print "Too many arguments, no attributes set."
        else:
            print "Empty object created."
            self.name = ""
            self.yeast = ""
            self.producer = ""
            self.id_code = ""
            self.attenuation = ""
            self.flocculation = ""
            self.ferment_temp = ""
            self.alcohol_yield = ""

        self.pitch_temp = ""
       

    def read_yeastfile(self):
        filename = open('yeast_list.pkl', 'rb')
        hashed_yeasts = pickle.load(filename)
        filename.close()
        return hashed_yeasts


    def write_yeastfile(self, yeasts_dict):
        filename = open('yeast_list.pkl', 'wb')
        pickle.dump(yeasts_dict, filename)
        filename.close()


    def add_yeast(self):
        if self.yeast == "":
            self.yeast = raw_input("what do you want to call it? > ")
        else:
            if raw_input("Do you want to call it %s? (y/n) > " % self.yeast).upper() != "Y":
                self.yeast = ""
                self.add_yeast()
        if self.producer == "":
            yeast_producer = raw_input("Who cultured the stuff? > ")
        else:
            yeast_producer = self.producer 
        if self.id_code == "":
            yeast_id_code = raw_input("what is the id_code, fool? > ")
        else:
            yeast_id_code = self.id_code 
        if self.attenuation == "":
            yeast_attenuation = raw_input("What is the attenuation? > ")
        else:
            yeast_attenuation = self.attenuation
        if self.flocculation == "":
            yeast_flocculation = raw_input("How does is flocculate? > ")
        else:
            yeast_flocculation = self.flocculation
        if self.ferment_temp == "":
            yeast_ferment_temp = raw_input("What temp does it ferment best at? > ")
        else:
            yeast_ferment_temp = self.ferment_temp
        if self.alcohol_yield == "":
            yeast_alcohol_yield = raw_input("How high of ABV will it ferment to? > ")
        else:
            yeast_alcohol_yield = self.alcohol_yield

        hashed_yeasts = self.read_yeastfile()
        hashed_yeasts[self.yeast] = ({'id_code': yeast_id_code,
                                     'producer': yeast_producer,
                                     'attenuation': yeast_attenuation,
                                     'ferment_temp': yeast_ferment_temp,
                                     'flocculation': yeast_flocculation,
                                     'alcohol_yield': yeast_alcohol_yield})
        self.write_yeastfile(hashed_yeasts)

        ###Do I want to return the added values to the object?
        #for key in self.__dict__.keys():
        #    self.__dict__[key] = hashed_yeasts[self.yeast][key]

        return "Created: ", (self.yeast, yeast_id_code)

    def remove_yeast(self):
        yeast_key = []
        if self.yeast == "":
            yeast_key.append(raw_input("what yeast do you want to remove? > "))
        else:
            yeast_key.append(self.yeast)
            self.select_yeast(yeast_key)
        hashed_yeasts = self.read_yeastfile()
        if self.yeast in hashed_yeasts:
            print ("Are you sure you want to remove: %s?"
                   % hashed_yeasts[self.yeast])
            answer = raw_input("(y/n) > ")
            if answer.upper() == ("Y"):
                del hashed_yeasts[self.yeast]
                self.write_yeastfile(hashed_yeasts)
                print "%s deleted." % self.yeast
                for key in self.__dict__.keys():
                    self.__dict__[key] = ""
            else:
                print "%s not deleted." %self.yeast
        else:
            print "Not found in list."


    def select_yeast(self, myList = [], *args):
        hashed_yeasts = self.read_yeastfile()
        input_list = []
        for x in myList:
            input_list.append(x)
        if len(input_list) >= 2:
            print "That could be any  of these:"
            for i in range(0, len(input_list) - 1):
                print "%s > %s, by %s" % (i, input_list[i], hashed_yeasts[input_list[i]]['producer'])

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
            self.select_yeast(input_list)
           
        elif len(input_list) == 1:
            output_list = []
            for key in hashed_yeasts:
                if input_list[0].upper() == key.upper():
                    print input_list[0]
                    if raw_input("Is it this one? (y/n) > ").upper() == "Y":
                        self.yeast = "%s" % input_list[0]
                        return
                elif input_list[0].upper() in key.upper():
                    output_list.append(key)
            if not output_list:
                if raw_input("Don\'t have that yeast. Want to add it? (y/n) > "
                            ).upper() == "Y":
                    self.add_yeast()
                else:
                    return "Yeast not added."
            self.select_yeast(output_list)

    def yeast(self):
        arguments = [raw_input("what yeast is this? > ")]
        self.select_yeast(arguments)
        return self.yeast


    def producer(self):
        hashed_yeasts = self.read_yeastfile()
        self.producer = hashed_yeasts[self.yeast]['producer']
        return hashed_yeasts[self.yeast]['producer']


    def id_code(self):
        hashed_yeasts = self.read_yeastfile()
        self.id_code = hashed_yeasts[self.yeast]['id_code']
        return hashed_yeasts[self.yeast]['id_code']


    def attenuation(self):
        hashed_yeasts = self.read_yeastfile()
        self.attenuation = hashed_yeasts[self.yeast]['attenuation']
        return hashed_yeasts[self.yeast]['attenuation']


    def flocculation(self):
        hashed_yeasts = self.read_yeastfile()
        self.flocculation = hashed_yeasts[self.yeast]['flocculation']
        return hashed_yeasts[self.yeast]['flocculation']


    def ferment_temp(self):
        hashed_yeasts = self.read_yeastfile()
        self.ferment_temp = hashed_yeasts[self.yeast]['ferment_temp']
        return hashed_yeasts[self.yeast]['ferment_temp']


    def alcohol_yield(self):
        hashed_yeasts = self.read_yeastfile()
        self.alcohol_yield = hashed_yeasts[self.yeast]['alcohol_yield']
        return hashed_yeasts[self.yeast]['alcohol_yield']

