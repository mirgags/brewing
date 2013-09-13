import pickle
import time


class Hop(object):

    def __init__(self, name):
        self.name = name


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
        hop_aau = raw_input("what is the alpha acid range sucka? > ")
        hop_origin = raw_input("where is it from? > ")
        hashed_hops = self.read_hopfile()
        hashed_hops[self.name.upper()] = {'aau': hop_aau, 'origin': hop_origin}
        self.write_hopfile(hashed_hops)

    def remove_hop(self):
        hashed_hops = self.read_hopfile()
        if self.name.upper() in hashed_hops:
            print "Are you sure you want to remove: %s?" % hashed_hops[self.name.upper()]
            answer = raw_input("(y/n) > ")
            if answer.startswith("y") == True:
                del hashed_hops[self.name.upper()]
                self.write_hopfile(hashed_hops)
                print "%s deleted." % self.name
        else:
            print "Not found in list."


    def aau(self):
        hop_name = self.name.upper()
        hashed_hops = self.read_hopfile()
        
        if not hop_name in hashed_hops:
            print "We ain\'t go tthat hop."
            self.add_hop()
            time.sleep(1)
            self.aau()
        if hop_name in hashed_hops:
            return hashed_hops[hop_name]['aau']


    def origin(self):
        hashed_hops = self.read_hopfile()
        filename.close()
        
        if not hop_name in hashed_hops:
            print "We ain\'t go tthat hop."
            self.add_hop(hop_name)
            self.origin()
        if hop_name in hashed_hops:
            return hashed_hops[hop_name]['origin']
