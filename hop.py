class Hop(object):

    def __init__(self, name):
        self.name = name


    def aau(self):
        hops = []
        hop_name = self.name.upper()
        with open('hop_list.txt') as hop_list:
            for line in hop_list:
                hops.append(eval(line.rstrip()))
        for hop in hops:
#            print hop['name']
#            print hop
            if (hop['name'].upper()).startswith(hop_name):
                print hop['aau']
                return hop['aau']


    def origin(self):
        with open('hop_list.txt') as hop_list:
            hops = []
            for line in hop_list:
                hops.append(line.rstrip())
        for hop in hops:
            if self.name.upper == startswith(hop['name'].upper):
                return hops['origin']

