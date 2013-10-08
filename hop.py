import pickle
import time
from recipe import *


class Hop(object):

    def __init__(self, *args):
        if len(args) > 0:
            if len(args) == 1:
                if raw_input("Do you want to use stored hop attributes? (y/n) > ").upper() == "Y":
                    hop_list = [args[0]]
                    self.select_hop(hop_list)
                    self.aau = self.aau()
                    self.origin = self.origin()
                    self.character = self.character()
                    self.name = args[0]
                    print "Object: %s created." % args[0]
                    
            else:
                self.hop = ""
                print "Too many arguments, no attributes set."
        else:
            print "Empty object created."
            self.name = ""
            self.hop = ""
            self.aau = ""
            self.origin = ""
            self.character = ""
        self.add_time = ""
        self.ounces = ""
       

    def read_hopfile(self):
        filename = open('hop_list.pkl', 'rb')
        hashed_hops = pickle.load(filename)
        filename.close()
        return hashed_hops


    def write_hopfile(self, hops_dict):
        filename = open('hop_list.pkl', 'wb')
        pickle.dump(hops_dict, filename)
        filename.close()


    def add_hop(self):
        if self.hop == "":
            self.hop = raw_input("what do you want to call it? > ")
        else:
            if raw_input("Do you want to call it %s? (y/n) > " % self.hop).upper() != "Y":
                self.hop = ""
                self.add_hop()
        if self.aau == "":
            hop_aau = raw_input("what is the aau rating, fool? > ")
        else:
            hop_aau = self.aau 
        if self.origin == "":
            hop_origin = raw_input("What is the origin? > ")
        else:
            hop_origin = self.origin
        if self.character == "":
            hop_character = raw_input("Got any clever comments about it? > ")
        else:
            hop_character = self.character
        hashed_hops = self.read_hopfile()
        hashed_hops[self.hop] = ({'aau': hop_aau,
                                  'origin': hop_origin,
                                  'character': hop_character})
        self.write_hopfile(hashed_hops)

        ###Do I want to return the added values to the object?
        #for key in self.__dict__.keys():
        #    self.__dict__[key] = hashed_hops[self.hop][key]

        return "Created: ", (self.hop, hop_aau, hop_origin)

    def remove_hop(self):
        hop_key = []
        if self.hop == "":
            hop_key.append(raw_input("what hop do you want to remove? > "))
        else:
            hop_key.append(self.hop)
            self.select_hop(hop_key)
        hashed_hops = self.read_hopfile()
        if self.hop in hashed_hops:
            print ("Are you sure you want to remove: %s?"
                   % hashed_hops[self.hop])
            answer = raw_input("(y/n) > ")
            if answer.upper() == ("Y"):
                del hashed_hops[self.hop]
                self.write_hopfile(hashed_hops)
                print "%s deleted." % self.hop
                for key in self.__dict__.keys():
                    self.__dict__[key] = ""
            else:
                print "%s not deleted." % self.hop
        else:
            print "Not found in list."


    def select_hop(self, myList = [], *args):
        hashed_hops = self.read_hopfile()
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
            self.select_hop(input_list)
           
        elif len(input_list) == 1:
            output_list = []
            for key in hashed_hops:
                if input_list[0].upper() == key.upper():
                    print input_list[0]
                    if raw_input("Is it this one? (y/n) > ").upper() == "Y":
                        self.hop = "%s" % input_list[0]
                        # return the list maybe? for the tester?
                        return
                elif input_list[0].upper() in key.upper():
                    output_list.append(key)
            if not output_list:
                if raw_input("Don\'t have that hop. Want to add it? (y/n) > "
                            ).upper() == "Y":
                    self.add_hop()
                else:
                    print "Hop not added."
                    super(Hop, self)
            self.select_hop(output_list)

    def hop(self):
        arguments = [raw_input("what hop is this? > ")]
        self.select_hop(arguments)
        return self.hop

    def aau(self):
        hashed_hops = self.read_hopfile()
        self.aau = hashed_hops[self.hop]['aau']
        return hashed_hops[self.hop]['aau']


    def origin(self):
        hashed_hops = self.read_hopfile()
        self.origin = hashed_hops[self.hop]['origin']
        return hashed_hops[self.hop]['origin']


    def character(self):
        hashed_hops = self.read_hopfile()
        self.character = hashed_hops[self.hop]['character']
        return hashed_hops[self.hop]['character']

